
document.addEventListener('DOMContentLoaded', function() {
    const btn = document.getElementById('myButton');
    if (btn) {
        btn.addEventListener('click', () => {
            alert('Hello from JavaScript!');
        });
    }
});
