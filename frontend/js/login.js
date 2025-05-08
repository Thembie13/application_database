// Add an event listener for the form submission
document.getElementById('loginForm').addEventListener('submit', function(e) {
  // Prevent the default form submission (which would reload the page)
  e.preventDefault();

  // Get the value entered in the email field (trimmed)
  const email = document.getElementById('email').value.trim();
  // Get the value entered in the password field
  const password = document.getElementById('password').value;
  // Get the selected role from the dropdown
  const role = document.getElementById('role').value;

  // Check if a role has been selected; if not, show an alert and stop
  if (!role) {
    alert('Please select a role.');
    return;
  }

  // For demonstration: show the entered data in an alert
  alert(`Email: ${email}\nPassword: ${'*'.repeat(password.length)}\nRole: ${role}`);

});
