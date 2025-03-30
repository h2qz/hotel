"""
This module contains the GuestService and Feedback classes for the Royal Stay Hotel Management System.
"""

import uuid
from datetime import datetime

class GuestService:
    """
    GuestService class representing additional services requested by guests.
    """
    
    def __init__(self, service_type, description, charge):
        """Initialize a new GuestService instance."""
        self._service_id = str(uuid.uuid4())[:8]  # Generate a short unique ID
        self._service_type = service_type
        self._description = description
        self._charge = charge
        self._status = "Requested"
        self._request_time = datetime.now()
        self._completion_time = None
    
    def get_service_id(self):
        """Get the service ID."""
        return self._service_id
    
    def get_service_type(self):
        """Get the service type."""
        return self._service_type
    
    def get_description(self):
        """Get the service description."""
        return self._description
    
    def get_charge(self):
        """Get the service charge."""
        return self._charge
    
    def get_status(self):
        """Get the service status."""
        return self._status
    
    def set_status(self, status):
        """Set a new status for the service."""
        self._status = status
        if status == "Completed":
            self._completion_time = datetime.now()
    
    def track_service_status(self):
        """Get the current status of the service request."""
        if self._status == "Completed" and self._completion_time:
            time_diff = self._completion_time - self._request_time
            minutes = time_diff.total_seconds() / 60
            return f"{self._status} (Response time: {minutes:.1f} minutes)"
        return self._status
    
    def __str__(self):
        """Return a string representation of the service."""
        return (f"Service: {self._service_type} (ID: {self._service_id}) | "
                f"Description: {self._description} | "
                f"Charge: ${self._charge:.2f} | "
                f"Status: {self._status}")


class Feedback:
    """
    Feedback class representing guest reviews and ratings.
    """
    
    def __init__(self, guest, booking, rating, comments):
        """Initialize a new Feedback instance."""
        self._feedback_id = f"FB-{booking.get_booking_id()}"
        self._guest = guest
        self._booking = booking
        self._rating = rating
        self._comments = comments
        self._submission_time = datetime.now()
    
    def get_feedback_id(self):
        """Get the feedback ID."""
        return self._feedback_id
    
    def get_guest(self):
        """Get the guest who provided the feedback."""
        return self._guest
    
    def get_booking(self):
        """Get the associated booking."""
        return self._booking
    
    def get_rating(self):
        """Get the numerical rating."""
        return self._rating
    
    def set_rating(self, rating):
        """Set a new rating."""
        if rating < 1 or rating > 5:
            raise ValueError("Rating must be between 1 and 5")
        self._rating = rating
    
    def get_comments(self):
        """Get the feedback comments."""
        return self._comments
    
    def set_comments(self, comments):
        """Set new feedback comments."""
        self._comments = comments
    
    def __str__(self):
        """Return a string representation of the feedback."""
        return (f"Feedback for Booking #{self._booking.get_booking_id()} | "
                f"Guest: {self._guest.get_name()} | "
                f"Rating: {self._rating}/5 | "
                f"Comments: {self._comments}")