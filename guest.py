"""
This module contains the Guest and LoyaltyProgram classes for the Royal Stay Hotel Management System.
"""

class Guest:
    """
    Guest class representing a hotel guest.
    """
    
    def __init__(self, guest_id, name, contact_info, email):
        """Initialize a new Guest instance."""
        self._guest_id = guest_id
        self._name = name
        self._contact_info = contact_info
        self._email = email
        self._loyalty_status = "Regular"
        self._booking_history = []
        self._loyalty_program = None
    
    def get_guest_id(self):
        """Get the guest ID."""
        return self._guest_id
    
    def get_name(self):
        """Get the guest's name."""
        return self._name
    
    def get_email(self):
        """Get the guest's email."""
        return self._email
    
    def set_email(self, email):
        """Set a new email for the guest."""
        if "@" not in email:
            raise ValueError("Invalid email format")
        self._email = email
    
    def get_loyalty_status(self):
        """Get the guest's loyalty status."""
        return self._loyalty_status
    
    def enroll_in_loyalty_program(self):
        """Enroll the guest in the loyalty program."""
        if not self._loyalty_program:
            self._loyalty_program = LoyaltyProgram(self._guest_id)
            return True
        return False
    
    def get_loyalty_program(self):
        """Get the guest's loyalty program."""
        return self._loyalty_program
    
    def create_booking(self, room, check_in, check_out):
        """
        Create a new booking for the guest.
        
        Returns:
            Booking: New booking object if successful
        """
        # Import here to avoid circular import issues
        from booking import Booking
        
        if room.check_availability(check_in, check_out):
            booking = Booking(len(self._booking_history) + 1, self, room, check_in, check_out)
            self._booking_history.append(booking)
            
            # Update room availability
            current_date = check_in
            while current_date < check_out:
                room.set_availability(current_date, False)
                # Move to next day
                current_date = current_date.replace(day=current_date.day + 1)
            
            return booking
        return None
    
    def view_history(self):
        """Get the guest's booking history."""
        return self._booking_history
    
    def __str__(self):
        """Return a string representation of the guest."""
        return f"Guest: {self._name} (ID: {self._guest_id}) | Status: {self._loyalty_status} | Contact: {self._contact_info}"


class LoyaltyProgram:
    """
    LoyaltyProgram class representing a hotel loyalty rewards program.
    """
    
    def __init__(self, guest_id):
        """Initialize a new LoyaltyProgram instance."""
        self._guest_id = guest_id
        self._points_balance = 0
        self._membership_level = "Bronze"
    
    def get_points_balance(self):
        """Get the current points balance."""
        return self._points_balance
    
    def get_membership_level(self):
        """Get the current membership level."""
        return self._membership_level
    
    def earn_points(self, amount):
        """Add points based on spending amount."""
        # Earn 10 points per dollar spent
        points_earned = int(amount * 10)
        self._points_balance += points_earned
        self._update_membership_level()
        return points_earned
    
    def redeem_points(self, points):
        """Redeem points for a discount."""
        if points > self._points_balance:
            raise ValueError("Not enough points available")
        
        # 100 points = $1 discount
        discount = points / 100
        self._points_balance -= points
        return discount
    
    def _update_membership_level(self):
        """Update membership level based on points."""
        if self._points_balance >= 5000:
            self._membership_level = "Gold"
        elif self._points_balance >= 1000:
            self._membership_level = "Silver"
        else:
            self._membership_level = "Bronze"
    
    def __str__(self):
        """Return a string representation of the loyalty program."""
        return f"Loyalty Program: Level: {self._membership_level} | Points: {self._points_balance}"