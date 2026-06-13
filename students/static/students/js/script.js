
// document.addEventListener('DOMContentLoaded', function() {
//     const btn = document.getElementById('myButton');
//     if (btn) {
//         btn.addEventListener('click', () => {
//             alert('Hello from JavaScript!');
//         });
//     }
// });


// Example: show toast message if Django messages framework is used
document.addEventListener('DOMContentLoaded', function() {
    // Auto-hide alerts after 3 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.transition = 'opacity 0.5s';
            alert.style.opacity = '0';
            setTimeout(() => alert.remove(), 500);
        }, 3000);
    });
});