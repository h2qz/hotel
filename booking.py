"""
This module contains the Booking and Invoice classes for the Royal Stay Hotel Management System.
"""

from datetime import datetime

class Booking:
    """
    Booking class representing a room reservation.
    """
    
    def __init__(self, booking_id, guest, room, check_in, check_out):
        """Initialize a new Booking instance."""
        self._booking_id = booking_id
        self._guest = guest
        self._room = room
        self._check_in = check_in
        self._check_out = check_out
        self._status = "Confirmed"
        self._invoice = None
        self._services = []
    
    def get_booking_id(self):
        """Get the booking ID."""
        return self._booking_id
    
    def get_guest(self):
        """Get the guest who made the booking."""
        return self._guest
    
    def get_room(self):
        """Get the booked room."""
        return self._room
    
    def get_check_in(self):
        """Get the check-in date."""
        return self._check_in
    
    def get_check_out(self):
        """Get the check-out date."""
        return self._check_out
    
    def get_status(self):
        """Get the booking status."""
        return self._status
    
    def set_status(self, status):
        """Set a new status for the booking."""
        self._status = status
    
    def calculate_stay_duration(self):
        """Calculate the duration of the stay in days."""
        delta = self._check_out - self._check_in
        return delta.days
    
    def add_service(self, service):
        """Add a service to the booking."""
        self._services.append(service)
    
    def get_services(self):
        """Get all services requested for this booking."""
        return self._services
    
    def generate_invoice(self):
        """
        Generate an invoice for the booking.
        
        Returns:
            Invoice: New invoice object
        """
        if not self._invoice:
            # Calculate base amount
            nights = self.calculate_stay_duration()
            base_amount = nights * self._room.get_price_per_night()
            
            # Add service charges
            service_charges = sum(service.get_charge() for service in self._services)
            
            total_amount = base_amount + service_charges
            
            # Create invoice
            self._invoice = Invoice(self._booking_id, total_amount)
            
            # Apply loyalty discount if applicable
            loyalty_program = self._guest.get_loyalty_program()
            if loyalty_program:
                if loyalty_program.get_membership_level() == "Silver":
                    self._invoice.apply_discount(5)
                elif loyalty_program.get_membership_level() == "Gold":
                    self._invoice.apply_discount(10)
        
        return self._invoice
    
    def cancel_reservation(self):
        """
        Cancel the booking and update room availability.
        
        Returns:
            bool: True if cancellation successful
        """
        if self._status == "Cancelled":
            return False
        
        # Update status
        self._status = "Cancelled"
        
        # Update room availability
        current_date = self._check_in
        while current_date < self._check_out:
            self._room.set_availability(current_date, True)
            # Move to next day
            current_date = current_date.replace(day=current_date.day + 1)
        
        return True
    
    def __str__(self):
        """Return a string representation of the booking."""
        return (f"Booking #{self._booking_id} | "
                f"Guest: {self._guest.get_name()} | "
                f"Room: {self._room.get_room_number()} | "
                f"Check-in: {self._check_in.strftime('%Y-%m-%d')} | "
                f"Check-out: {self._check_out.strftime('%Y-%m-%d')} | "
                f"Status: {self._status}")


class Invoice:
    """
    Invoice class representing a booking invoice.
    """
    
    def __init__(self, booking_id, total_amount):
        """Initialize a new Invoice instance."""
        self._invoice_id = f"INV-{booking_id}"
        self._booking_id = booking_id
        self._total_amount = total_amount
        self._discount_applied = 0
        self._final_amount = total_amount
        self._payment_status = "Pending"
    
    def get_invoice_id(self):
        """Get the invoice ID."""
        return self._invoice_id
    
    def get_total_amount(self):
        """Get the total amount before discount."""
        return self._total_amount
    
    def get_discount_applied(self):
        """Get the discount percentage applied."""
        return self._discount_applied
    
    def get_final_amount(self):
        """Get the final amount after discount."""
        return self._final_amount
    
    def get_payment_status(self):
        """Get the payment status."""
        return self._payment_status
    
    def set_payment_status(self, status):
        """Set a new payment status."""
        self._payment_status = status
    
    def apply_discount(self, discount_percent):
        """Apply a discount to the invoice."""
        if discount_percent < 0 or discount_percent > 100:
            raise ValueError("Discount must be between 0 and 100 percent")
        
        self._discount_applied = discount_percent
        discount_amount = (self._total_amount * discount_percent) / 100
        self._final_amount = self._total_amount - discount_amount
    
    def calculate_total(self):
        """Calculate the final amount to pay."""
        return self._final_amount
    
    def __str__(self):
        """Return a string representation of the invoice."""
        return (f"Invoice: {self._invoice_id} | "
                f"Booking: {self._booking_id} | "
                f"Total: ${self._total_amount:.2f} | "
                f"Discount: {self._discount_applied}% | "
                f"Final Amount: ${self._final_amount:.2f} | "
                f"Status: {self._payment_status}")