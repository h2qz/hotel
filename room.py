"""
This module contains the Room class and its subclasses for the Royal Stay Hotel Management System.
"""

from datetime import datetime

class Room:
    """
    Base class for all room types in the hotel.
    """
    
    def __init__(self, room_number, room_type, price_per_night, amenities):
        """Initialize a new Room instance."""
        self._room_number = room_number
        self._room_type = room_type
        self._price_per_night = price_per_night
        self._amenities = amenities
        self._availability = {}  # Dictionary to track availability by date
    
    def get_room_number(self):
        """Get the room number."""
        return self._room_number
    
    def get_room_type(self):
        """Get the room type."""
        return self._room_type
    
    def get_price_per_night(self):
        """Get the price per night."""
        return self._price_per_night
    
    def set_price_per_night(self, price):
        """Set a new price per night for the room."""
        if price < 0:
            raise ValueError("Price cannot be negative")
        self._price_per_night = price
    
    def get_amenities(self):
        """Get the list of amenities."""
        return self._amenities
    
    def check_availability(self, check_in, check_out):
        """Check if the room is available for the given dates."""
        if check_out <= check_in:
            raise ValueError("Check-out date must be after check-in date")
        
        current_date = check_in
        while current_date < check_out:
            date_str = current_date.strftime("%Y-%m-%d")
            if date_str in self._availability and not self._availability[date_str]:
                return False
            current_date = datetime(current_date.year, current_date.month, 
                                  current_date.day + 1)
        return True
    
    def set_availability(self, date, is_available):
        """Set the availability status for a specific date."""
        date_str = date.strftime("%Y-%m-%d")
        self._availability[date_str] = is_available
    
    def __str__(self):
        """Return a string representation of the room."""
        amenities_str = ", ".join(self._amenities)
        return f"Room {self._room_number} ({self._room_type}): ${self._price_per_night:.2f}/night | Amenities: {amenities_str}"


class SingleRoom(Room):
    """Room with a single bed."""
    
    def __init__(self, room_number, price_per_night, amenities, bed_type):
        """Initialize a SingleRoom instance."""
        super().__init__(room_number, "Single", price_per_night, amenities)
        self._bed_type = bed_type
    
    def get_bed_type(self):
        """Get the bed type."""
        return self._bed_type
    
    def get_discount(self):
        """Calculate discount for single rooms."""
        return 5.0  # 5% discount
    
    def __str__(self):
        """Return a string representation of the single room."""
        return f"{super().__str__()} | Bed Type: {self._bed_type}"


class DoubleRoom(Room):
    """Room with double beds."""
    
    def __init__(self, room_number, price_per_night, amenities, extra_bed_option=False):
        """Initialize a DoubleRoom instance."""
        super().__init__(room_number, "Double", price_per_night, amenities)
        self._extra_bed_option = extra_bed_option
        self._extra_bed_requested = False
    
    def request_extra_bed(self):
        """Request an extra bed for the room."""
        if self._extra_bed_option and not self._extra_bed_requested:
            self._extra_bed_requested = True
            return True
        return False
    
    def __str__(self):
        """Return a string representation of the double room."""
        extra_bed_str = "Extra bed available" if self._extra_bed_option else "No extra bed option"
        if self._extra_bed_requested:
            extra_bed_str += " (Requested)"
        return f"{super().__str__()} | {extra_bed_str}"


class Suite(Room):
    """Luxury suite room."""
    
    def __init__(self, room_number, price_per_night, amenities, suite_type):
        """Initialize a Suite instance."""
        super().__init__(room_number, "Suite", price_per_night, amenities)
        self._suite_type = suite_type
    
    def get_suite_type(self):
        """Get the suite type."""
        return self._suite_type
    
    def get_upgrades(self):
        """Get available upgrades for the suite."""
        # Simplified upgrades based on suite type
        if self._suite_type == "Executive":
            return [("Business Services", 100.0), ("Airport Transfer", 80.0)]
        else:  # Junior or Presidential
            return [("Premium Service", 150.0)]
    
    def __str__(self):
        """Return a string representation of the suite."""
        return f"{super().__str__()} | Suite Type: {self._suite_type}"