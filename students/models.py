from django.db import models

# Create your models here.
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    course = models.CharField(max_length=100)

    def __str__(self):
        return self.name
from django.db import models

class Student(models.Model):
    roll_no = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    class_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='student_photos/', blank=True, null=True)

    def __str__(self):
        return self.name