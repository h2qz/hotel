"""
Test cases for the Royal Stay Hotel Management System.
"""

from datetime import datetime, timedelta
import sys
import os

# Import the necessary modules
from room import Room, SingleRoom, DoubleRoom, Suite
from guest import Guest, LoyaltyProgram
from booking import Booking, Invoice
from payment import Payment
from services import GuestService, Feedback

def test_guest_account_creation():
    """Test the process of guest account creation."""
    print("\n=== Test: Guest Account Creation ===")
    
    # Test Case 1: Create a new guest
    print("\nTest Case 1: Create a new guest")
    guest1 = Guest(1, "John Smith", "555-123-4567", "john.smith@example.com")
    print(guest1)
    
    # Test Case 2: Enroll in loyalty program
    print("\nTest Case 2: Enroll in loyalty program")
    guest1.enroll_in_loyalty_program()
    loyalty = guest1.get_loyalty_program()
    print(f"Loyalty program: {loyalty}")
    
    return guest1

def test_room_management():
    """Test room creation and availability checking."""
    print("\n=== Test: Room Management ===")
    
    # Test Case 1: Create different room types
    print("\nTest Case 1: Create different room types")
    single_room = SingleRoom(101, 100.0, ["Wi-Fi", "TV"], "Queen")
    double_room = DoubleRoom(201, 150.0, ["Wi-Fi", "TV", "Mini-bar"], True)
    suite = Suite(301, 300.0, ["Wi-Fi", "TV", "Jacuzzi"], "Executive")
    
    print(single_room)
    print(double_room)
    print(suite)
    
    # Test Case 2: Check room availability
    print("\nTest Case 2: Check room availability")
    today = datetime.now()
    tomorrow = today + timedelta(days=1)
    next_week = today + timedelta(days=7)
    
    # Set availability for today
    single_room.set_availability(today, True)
    
    # Check availability
    is_available = single_room.check_availability(today, tomorrow)
    print(f"Room available today to tomorrow: {is_available}")
    
    return [single_room, double_room, suite]

def test_making_reservation(guest, rooms):
    """Test the reservation process."""
    print("\n=== Test: Making a Room Reservation ===")
    
    # Test Case 1: Make a successful reservation
    print("\nTest Case 1: Make a successful reservation")
    check_in = datetime.now() + timedelta(days=1)
    check_out = check_in + timedelta(days=3)
    
    room = rooms[0]  # Single room
    booking = guest.create_booking(room, check_in, check_out)
    
    if booking:
        print(f"Booking successful: {booking}")
        print(f"Stay duration: {booking.calculate_stay_duration()} nights")
    else:
        print("Booking failed")
    
    # Test Case 2: Try to book the same room for overlapping dates
    print("\nTest Case 2: Try to book the same room for overlapping dates")
    guest2 = Guest(2, "Jane Doe", "555-987-6543", "jane.doe@example.com")
    another_booking = guest2.create_booking(room, check_in, check_out)
    
    if another_booking:
        print(f"Second booking successful: {another_booking}")
    else:
        print("Second booking failed - room not available for requested dates")
    
    return booking

def test_invoice_and_payment(booking):
    """Test invoice generation and payment processing."""
    print("\n=== Test: Invoice Generation and Payment ===")
    
    # Test Case 1: Add a service to the booking
    print("\nTest Case 1: Add a service to the booking")
    room_service = GuestService("Room Service", "Dinner for two", 75.0)
    booking.add_service(room_service)
    print(f"Service added: {room_service}")
    
    # Test Case 2: Generate invoice
    print("\nTest Case 2: Generate invoice")
    invoice = booking.generate_invoice()
    print(f"Invoice generated: {invoice}")
    
    # Test Case 3: Process payment
    print("\nTest Case 3: Process payment")
    payment = Payment(invoice, invoice.get_final_amount(), "Credit Card")
    success = payment.process_payment()
    
    print(f"Payment successful: {success}")
    print(f"Payment details: {payment}")
    print(f"Invoice status: {invoice.get_payment_status()}")
    
    # Test Case 4: Generate receipt
    print("\nTest Case 4: Generate receipt")
    receipt = payment.generate_receipt()
    print(receipt)
    
    return invoice

def test_feedback_system(guest, booking):
    """Test the feedback and review system."""
    print("\n=== Test: Feedback System ===")
    
    # Test Case 1: Submit feedback
    print("\nTest Case 1: Submit feedback")
    feedback = Feedback(guest, booking, 4, "Great room and service! Very comfortable.")
    print(f"Feedback submitted: {feedback}")
    
    # Test Case 2: Update feedback
    print("\nTest Case 2: Update feedback")
    feedback.set_rating(5)
    feedback.set_comments("Even better than I initially thought! Highly recommend.")
    print(f"Updated feedback: {feedback}")
    
    return feedback

def test_loyalty_program(guest, invoice):
    """Test the loyalty program functionality."""
    print("\n=== Test: Loyalty Program ===")
    
    loyalty = guest.get_loyalty_program()
    if not loyalty:
        print("Guest not enrolled in loyalty program")
        return
    
    # Test Case 1: Earn points from invoice
    print("\nTest Case 1: Earn points from invoice")
    points_earned = loyalty.earn_points(invoice.get_final_amount())
    print(f"Points earned: {points_earned}")
    print(f"New points balance: {loyalty.get_points_balance()}")
    print(f"Membership level: {loyalty.get_membership_level()}")
    
    # Test Case 2: Redeem points
    print("\nTest Case 2: Redeem points")
    if loyalty.get_points_balance() >= 500:
        discount = loyalty.redeem_points(500)
        print(f"Redeemed 500 points for ${discount:.2f} discount")
        print(f"Remaining points: {loyalty.get_points_balance()}")
    else:
        print("Not enough points to redeem")

def main():
    """Run all tests."""
    print("==== ROYAL STAY HOTEL MANAGEMENT SYSTEM TESTS ====")
    
    # Run tests sequentially, passing objects between tests
    guest = test_guest_account_creation()
    rooms = test_room_management()
    booking = test_making_reservation(guest, rooms)
    invoice = test_invoice_and_payment(booking)
    feedback = test_feedback_system(guest, booking)
    test_loyalty_program(guest, invoice)
    
    print("\n==== All tests completed ====")

if __name__ == "__main__":
    main()