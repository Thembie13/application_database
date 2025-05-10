// Get user role from localStorage
const userRole = localStorage.getItem('role') || 'renter';

// Elements to show/hide
const paymentsLink = document.getElementById('payments-link');
const managePropertiesLink = document.getElementById('manage-properties-link');
const bookingSection = document.getElementById('booking-section');
const agentActionsSection = document.getElementById('agent-actions-section');

// Show/hide top nav links
if (userRole === 'renter') {
  paymentsLink.style.display = 'inline';
  managePropertiesLink.style.display = 'none';
} else if (userRole === 'agent') {
  paymentsLink.style.display = 'none';
  managePropertiesLink.style.display = 'inline';
}

// Set username
document.getElementById('user-name').textContent =
  localStorage.getItem('username') || "User";

// Show/hide booking or management sections
if (userRole === 'renter') {
  bookingSection.style.display = 'block';
  agentActionsSection.style.display = 'none';
} else if (userRole === 'agent') {
  bookingSection.style.display = 'none';
  agentActionsSection.style.display = 'block';
} else {
  bookingSection.style.display = 'none';
  agentActionsSection.style.display = 'none';
}
