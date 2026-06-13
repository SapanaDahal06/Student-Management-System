from django.shortcuts import render, get_object_or_404, redirect
from .models import Student
from .forms import StudentForm

# ----- Home page (optional – you can remove if using dashboard as home) -----
def home(request):
    from .models import Student
    context = {
        'total_students': Student.objects.count(),
        'total_teachers': 0,
        'total_classes': 0,
        'pending_fees': 0,
    }
    return render(request, 'home.html', context)


    from .models import Student
    context = {
        'total_students': Student.objects.count(),
        'total_teachers': 0,   # replace with actual model
        'total_classes': 0,    # replace
        'pending_fees': 0,     # replace
    }
    return render(request, 'home.html', context)

# ----- Dashboard (main landing page) -----
def dashboard(request):
    context = {
        'total_students': Student.objects.count(),
        'recent_students': Student.objects.order_by('-id')[:5],
    }
    return render(request, 'dashboard.html', context)

# ----- Student CRUD views -----
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form, 'form_title': 'Add Student'})

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'student_detail.html', {'student': student})

def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_form.html', {'form': form, 'form_title': 'Edit Student'})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return redirect('student_list')