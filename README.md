---

# **Royal Stay Hotel Management System**

## **Overview**

The **Royal Stay Hotel Management System** is a comprehensive solution for managing hotel operations. The system allows hotel staff and guests to interact seamlessly through features such as room management, guest reservations, invoicing, loyalty programs, guest services, and feedback management. It is designed to improve the guest experience, streamline hotel operations, and support key functionalities that a modern hotel management system needs.

---

## **Features**

- **Room Management**: Manage room details including type, price, availability, and amenities.
- **Guest Management**: Create and manage guest accounts, update profiles, and track loyalty status.
- **Booking System**: Allows guests to search and book rooms, view availability, and receive booking confirmations.
- **Payment and Invoicing**: Handles payment processing, generates invoices, and supports multiple payment methods (credit card, mobile wallet).
- **Loyalty Rewards Program**: Tracks and rewards loyal guests with points, redeemable for discounts or free services.
- **Guest Services and Requests**: Allows guests to request services (e.g., room service, housekeeping) during their stay.
- **Feedback and Reviews**: Collects and manages guest feedback and reviews for continuous service improvement.

---

## **System Design**

The system is based on **Object-Oriented Programming (OOP)** principles and consists of several interconnected modules:

- **Guest Management**: Handles all guest-related information and activities, including loyalty program tracking.
- **Room and Booking**: Manages the room inventory, availability, and reservation system.
- **Payment and Invoicing**: Ensures proper payment handling and invoice generation.
- **Loyalty Program**: Enables guests to earn and redeem loyalty points.
- **Guest Services**: Allows guests to interact with hotel services during their stay.
- **Reviews**: Collects guest feedback to improve services.

---

## **Technologies Used**

- **Python**: The backend programming language used for implementing the system's core logic.
- **OOP (Object-Oriented Programming)**: The system is designed using OOP principles to ensure modularity, reusability, and easy maintenance.
- **UML**: The system was designed using Unified Modeling Language (UML) to represent class structures and relationships clearly.

---

## **Setup Instructions**

### **1. Clone the Repository**
To get started, clone this repository to your local machine using the following command:


### **2. Install Dependencies**
Ensure you have Python 3.x installed on your machine. You can install the required dependencies using **pip** (if needed, create a virtual environment first):

```bash
pip install -r requirements.txt
```

### **3. Run the System**
To run the system, simply execute the **main.py** script:

```bash
python main.py
```

---

## **Usage Examples**

### **1. Guest Account Creation**
You can create a guest account by providing the necessary information:

```python
guest = Guest("John Doe", "john.doe@example.com", "123-456-7890")
guest.create_account("johndoe", "password123")
```

### **2. Booking a Room**
Guests can view available rooms and make a reservation:

```python
room = Room("101", "Single", 100.0, True, ["Wi-Fi", "TV"])
booking = Booking(guest, room, "2025-04-01", "2025-04-05")
booking.confirm_booking()
```

### **3. Generating an Invoice**
Once the booking is confirmed, an invoice can be generated:

```python
invoice = Invoice(booking)
invoice.generate_invoice()
```

---

## **Test Cases**

The system includes several **test cases** to validate the functionality of each module. You can run the tests to ensure that the system behaves as expected:

```bash
python test.py
```

Test cases include:
- **Guest account creation**
- **Room search and booking**
- **Payment and invoicing**
- **Loyalty program points**
- **Guest services and requests**
- **Review submission**

---

## **Contributing**

We welcome contributions! If you'd like to improve the system, follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-name`).
6. Open a pull request to the **main** branch.

---

