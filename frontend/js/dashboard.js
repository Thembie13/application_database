// Example: Simulate getting the user's role from session/localStorage
// In a real app, replace this with actual authentication logic
// Possible values: "renter" or "agent"
const userRole = localStorage.getItem('role') || 'renter'; // Default to renter for demo

// Get references to role-specific elements
const renterBookingsLink = document.getElementById('renter-bookings-link');
const agentBookingsLink = document.getElementById('agent-bookings-link');
const managePropertiesLink = document.getElementById('manage-properties-link');
const paymentLink = document.getElementById('payment-link');
const dashboardMessage = document.getElementById('dashboard-message');

// Show/hide links and set messages based on user role
if (userRole === 'renter') {
  // Show renter-specific links, hide agent ones
  renterBookingsLink.style.display = 'inline';
  agentBookingsLink.style.display = 'none';
  managePropertiesLink.style.display = 'none';
  paymentLink.style.display = 'list-item';
  dashboardMessage.textContent = "You are logged in as a Renter. Here you can search properties, book, and manage your bookings and payment info.";
} else if (userRole === 'agent') {
  // Show agent-specific links, hide renter ones
  renterBookingsLink.style.display = 'none';
  agentBookingsLink.style.display = 'inline';
  managePropertiesLink.style.display = 'list-item';
  paymentLink.style.display = 'none';
  dashboardMessage.textContent = "You are logged in as an Agent. Here you can manage your properties and view bookings for your listings.";
}
