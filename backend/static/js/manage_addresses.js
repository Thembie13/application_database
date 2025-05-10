// Show the add address form and clear fields
document.getElementById('show-add-address-form').onclick = function() {
  document.getElementById('address-form').classList.remove('hidden');
  document.getElementById('address-form-title').textContent = "Add Address";
  document.getElementById('address_id').value = "";
  document.getElementById('street').value = "";
  document.getElementById('city').value = "";
  document.getElementById('state').value = "";
  document.getElementById('zip').value = "";
};

// Hide the address form
function hideAddressForm() {
  document.getElementById('address-form').classList.add('hidden');
}
window.hideAddressForm = hideAddressForm;

// Edit address (you will fill this with data from your backend)
function editAddress(address_id) {
  // Example: fill fields with backend data for address_id
  document.getElementById('address-form').classList.remove('hidden');
  document.getElementById('address-form-title').textContent = "Edit Address";
  // Fill fields with address data here...
}
window.editAddress = editAddress;
