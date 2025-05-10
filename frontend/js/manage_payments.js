// Show the add payment form and clear fields
document.getElementById('show-add-form').onclick = function() {
  document.getElementById('payment-form').classList.remove('hidden');
  document.getElementById('form-title').textContent = "Add Payment Method";
  document.getElementById('payment_id').value = "";
  document.getElementById('cc-name').value = "";
  document.getElementById('cc-number').value = "";
  document.getElementById('cc-exp').value = "";
  document.getElementById('cc-cvc').value = "";
  document.getElementById('billing_address_id').selectedIndex = 0;
};

// Hide the payment form
function hidePaymentForm() {
  document.getElementById('payment-form').classList.add('hidden');
}
window.hidePaymentForm = hidePaymentForm;

// Edit payment (you will fill this with data from your backend)
function editPayment(payment_id) {
  // Example: fill fields with backend data for payment_id
  document.getElementById('payment-form').classList.remove('hidden');
  document.getElementById('form-title').textContent = "Edit Payment Method";
  // Fill fields with payment data here...
}
window.editPayment = editPayment;
