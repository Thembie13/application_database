document.getElementById('loginForm').addEventListener('submit', function(event) {
  event.preventDefault(); // Prevent default form submission

  const email = document.getElementById('email').value;
  const password = document.getElementById('password').value;
  const role = document.getElementById('role').value;

  // Basic validation
  if (!email || !password || !role) {
    alert("Please fill in all fields and select a role.");
    return;
  }

  // Simulate login 
  localStorage.setItem('role', role);

  // Redirect to dashboard
  window.location.href = '../html/dashboard.html'; //goes to dashboard 
});

// registration after click 
document.getElementById('registerButton').addEventListener('click', function() { 
  window.location.href = 'register.html'; // goes to registration 
}); 

