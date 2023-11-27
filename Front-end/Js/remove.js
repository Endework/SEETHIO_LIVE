var textArea = document.getElementById('removereson');
var other = document.getElementById('others');
textArea.style.display = 'none';
other.addEventListener('change', function() {
    if (this.checked) {
        textArea.style.display = 'block';
    } else {
        textArea.style.display = 'none';
    }
});
var closeButtons = document.getElementsByClassName('close'); // Note: no dot before 'close'

for (var i = 0; i < closeButtons.length; i++) {
    closeButtons[i].addEventListener('click', function() {
        other.checked = false;
        textArea.style.display='none';
    });
}

