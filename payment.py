"""
This module contains the Payment class for the Royal Stay Hotel Management System.
"""

import uuid
from datetime import datetime

class Payment:
    """
    Payment class representing a payment for a booking invoice.
    """
    
    def __init__(self, invoice, amount, payment_method):
        """Initialize a new Payment instance."""
        self._payment_id = str(uuid.uuid4())[:8]  # Generate a short unique ID
        self._invoice = invoice
        self._amount = amount
        self._payment_method = payment_method
        self._timestamp = datetime.now()
        self._status = "Pending"
    
    def get_payment_id(self):
        """Get the payment ID."""
        return self._payment_id
    
    def get_invoice(self):
        """Get the associated invoice."""
        return self._invoice
    
    def get_amount(self):
        """Get the payment amount."""
        return self._amount
    
    def get_payment_method(self):
        """Get the payment method."""
        return self._payment_method
    
    def get_status(self):
        """Get the payment status."""
        return self._status
    
    def process_payment(self):
        """
        Process the payment.
        
        Returns:
            bool: True if payment successful
        """
        # Check if amount matches invoice
        if self._amount < self._invoice.get_final_amount():
            self._status = "Failed - Insufficient Amount"
            return False
        
        # Process based on payment method
        if self._payment_method in ["Credit Card", "Cash", "Mobile Wallet"]:
            self._status = "Completed"
            self._invoice.set_payment_status("Paid")
            return True
        else:
            self._status = "Failed - Invalid Payment Method"
            return False
    
    def generate_receipt(self):
        """
        Generate a receipt for the payment.
        
        Returns:
            str: Receipt text
        """
        receipt = (
            f"RECEIPT\n"
            f"--------\n"
            f"Payment ID: {self._payment_id}\n"
            f"Invoice: {self._invoice.get_invoice_id()}\n"
            f"Date: {self._timestamp.strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"Amount: ${self._amount:.2f}\n"
            f"Method: {self._payment_method}\n"
            f"Status: {self._status}\n"
            f"--------\n"
            f"Thank you for choosing Royal Stay Hotel!"
        )
        return receipt
    
    def __str__(self):
        """Return a string representation of the payment."""
        return (f"Payment: {self._payment_id} | "
                f"Invoice: {self._invoice.get_invoice_id()} | "
                f"Amount: ${self._amount:.2f} | "
                f"Method: {self._payment_method} | "
                f"Status: {self._status}")