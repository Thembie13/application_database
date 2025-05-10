// Get user role from storage or default to 'renter'
const userRole = localStorage.getItem('role') || 'renter';

// Sidebar links
const paymentsLink = document.getElementById('payments-link');
const addressesLink = document.getElementById('addresses-link');
const manageLink = document.getElementById('manage-link');

// Dashboard sections
const renterDashboard = document.getElementById('renter-dashboard');
const agentDashboard = document.getElementById('agent-dashboard');

// Rewards points (simulate with a number; replace with real data)
const renterPoints = document.getElementById('renter-points');

// User profile dropdown logic
const userProfile = document.getElementById('user-profile');
const profileDropdown = document.getElementById('profile-dropdown');
let dropdownOpen = false;

userProfile.addEventListener('click', function() {
  dropdownOpen = !dropdownOpen;
  profileDropdown.style.display = dropdownOpen ? 'flex' : 'none';
});

document.addEventListener('click', function(event) {
  if (!userProfile.contains(event.target)) {
    profileDropdown.style.display = 'none';
    dropdownOpen = false;
  }
});

// Show/hide sidebar links and dashboard sections based on user role
if (userRole === 'renter') {
  paymentsLink.style.display = 'list-item';
  addressesLink.style.display = 'list-item';
  manageLink.style.display = 'none';
  renterDashboard.style.display = 'block';
  agentDashboard.style.display = 'none';
  renterPoints.textContent = "Points: 120";
} else if (userRole === 'agent') {
  paymentsLink.style.display = 'none';
  addressesLink.style.display = 'none';
  manageLink.style.display = 'list-item';
  agentDashboard.style.display = 'block';
  renterDashboard.style.display = 'none';
}

document.getElementById('user-name').textContent = localStorage.getItem('username') || "User";

