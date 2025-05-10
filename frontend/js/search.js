// Show/hide Payments or Manage Properties link based on user role
const userRole = localStorage.getItem('role') || 'renter'; // or 'agent'
const paymentsLink = document.getElementById('payments-link');
const managePropertiesLink = document.getElementById('manage-properties-link');

if (userRole === 'renter') {
  paymentsLink.style.display = 'inline';
  managePropertiesLink.style.display = 'none';
} else if (userRole === 'agent') {
  paymentsLink.style.display = 'none';
  managePropertiesLink.style.display = 'inline';
}

