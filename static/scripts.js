document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('button').forEach(button => {
        button.addEventListener('click', function() {
            this.classList.add('flash');
            setTimeout(() => this.classList.remove('flash'), 500);
        });
    });
});
