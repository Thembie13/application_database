// Wait for the registration form to be submitted
document.getElementById('registerForm').addEventListener('submit', function(e) {
  // Prevent the default form submission (which would reload the page)
  e.preventDefault();

  // Get the value entered in the name field (trimmed)
  const name = document.getElementById('name').value.trim();
  // Get the value entered in the email field (trimmed)
  const email = document.getElementById('email').value.trim();
  // Get the value entered in the password field
  const password = document.getElementById('password').value;
  // Get the selected role from the dropdown
  const role = document.getElementById('role').value;

  // Basic validation: check if a role has been selected
  if (!role) {
    alert('Please select a role.');
    return;
  }

  // Redirect to dashboard
  window.location.href = 'dashboard.html'; //goes to dashboard 
});
