document.getElementById('myForm').addEventListener('submit', function(event) {
    event.preventDefault();
    var email = document.getElementById('email');
    var password = document.getElementById('password1');
    var terms = document.getElementById('terms');
    var message = document.getElementById('message');

    // Clear previous messages and borders
    message.innerHTML = '';
    password.style.border = '';
    terms.style.border = '';

    // Check if all fields are filled
    if ( !email.value ||  !password.value || !terms.checked) {
        message.innerHTML += 'Please fill in all fields and agree to the terms and conditions.<br>';
        password.style.border = password.value ? '' : 'red';
        terms.style.border = terms.checked ? '' : '1px solid red';
        return false;
    }

    

    // Check password strength
    if (password.value.length < 8) {
        message.innerHTML += 'Your password is too weak. It should be at least 8 characters long.<br>';
        password.classList.add("border_invalid");
        return false;
    } else {
        password.classList.remove("border_invalid");
    }

    // Check terms and conditions
    if (!terms.checked) {
        message.innerHTML += 'Please agree to the terms and conditions.<br>';
        terms.classList.add("border_invalid");
        return false;
    } else {
        terms.classList.remove("border_invalid");
    }

    message.innerHTML += 'Form submitted successfully!';
});

document.getElementById('eye').addEventListener('click', function() {
  var password = document.getElementById('password1');
  if (password.type === 'password') {
      password.type = 'text';
  } else {
      password.type = 'password';
  }
});

