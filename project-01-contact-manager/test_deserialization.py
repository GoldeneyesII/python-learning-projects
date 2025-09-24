from person import Person, Address
from contact_manager import ContactManager
import json

print("=== Testing Deserialization ===")

# Test Address.from_dict first
address_data = {
    "number": "789", 
    "street": "Oak Blvd", 
    "street2": "Suite 100",
    "city": "Tacoma", 
    "state": "WA", 
    "zipcode": "98402"
}

print("Testing Address.from_dict:")
addr = Address.from_dict(address_data)
print(f"Created address: {addr}")
print()

# Test Person.from_dict  
person_data = {
    "name": "Test Person",
    "age": 25,
    "address": address_data
}

print("Testing Person.from_dict:")
person = Person.from_dict(person_data)
print(f"Created person: {person}")
print()

# Test full round-trip: save → load → verify
print("=== Testing Full Round-Trip ===")
manager = ContactManager("test_contacts.json")

# Add some contacts and save
addr1 = Address("123", "First St", "City1", "WA", "12345")
person1 = Person("Alice", 30, addr1)
manager.add_contact(person1)
manager.save_contacts()

# Create new manager and load
manager2 = ContactManager("test_contacts.json")
manager2.load_contacts()

print(f"Loaded contacts:")
for contact in manager2.contacts:
    print(contact)
