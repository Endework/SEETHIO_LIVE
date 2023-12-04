// Get the password input fields, submit button and message paragraph
var password1 = document.getElementById('password');
var password2 = document.getElementById('password-confirm');
var submitButton = document.getElementById('submit');
var message = document.getElementById('message');

// Add event listener to the submit button
submitButton.addEventListener('click', function(event) {
    // Prevent form from submitting
    event.preventDefault();

    // Reset styles and message
    password1.style.borderColor = '';
    password2.style.borderColor = '';
    message.innerHTML = '';

    // Check if both fields are not empty
    if (password1.value && password2.value) {
        // Check if passwords match
        if (password1.value === password2.value) {
            // Passwords match, check for password strength
            if (password1.value.length < 8) {
                message.innerHTML = 'Password is too short. It should be at least 8 characters long.';
            } else if (!/\d/.test(password1.value)) {
                message.innerHTML = 'Password should contain at least one number.';
            } else if (!/[a-z]/.test(password1.value)) {
                message.innerHTML = 'Password should contain at least one lowercase letter.';
            } else if (!/[A-Z]/.test(password1.value)) {
                message.innerHTML = 'Password should contain at least one uppercase letter.';
            } else {
                message.innerHTML = 'Password is strong.';
            }
        } else {
            // Passwords do not match, apply red border and show error message
            password1.style.borderColor = 'red';
            password2.style.borderColor = 'red';
            message.innerHTML = "Passwords don't match.";
        }
    } else {
        // One or both fields are empty, show error message
        message.innerHTML = 'Please enter a password in both fields.';
    }
});
