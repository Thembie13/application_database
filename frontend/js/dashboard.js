// Get user role from storage or default to 'renter'
const userRole = localStorage.getItem('role') || 'renter';

// Sidebar role-specific links
const renterBookingsLink = document.getElementById('renter-bookings-link');
const agentBookingsLink = document.getElementById('agent-bookings-link');
const managePropertiesLink = document.getElementById('manage-properties-link');
const paymentLink = document.getElementById('payment-link'); 

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

// Show/hide links and dashboard sections based on user role
if (userRole === 'renter') {
  renterBookingsLink.style.display = 'block';
  paymentLink.style.display = 'block';
  agentBookingsLink.style.display = 'none';
  managePropertiesLink.style.display = 'none';
  renterDashboard.style.display = 'block';
  agentDashboard.style.display = 'none';
  // Simulate points (replace with real logic)
  renterPoints.textContent = "Points: 120";
} else if (userRole === 'agent') {
  agentBookingsLink.style.display = 'block';
  managePropertiesLink.style.display = 'block';
  renterBookingsLink.style.display = 'none';
  paymentLink.style.display = 'none';
  agentDashboard.style.display = 'block';
  renterDashboard.style.display = 'none';
}

// Optionally, set the username in the profile (replace with real user data)
document.getElementById('user-name').textContent = localStorage.getItem('username') || "User";

