from person import Person, Address
from contact_manager import ContactManager

# Create some test contacts
addr1 = Address("123", "Main St", "Spokane", "WA", "99201")
addr2 = Address("456", "Pine Ave", "Seattle", "WA", "98101", "Apt 4B")

person1 = Person("John Doe", 31, addr1)
person2 = Person("Jane Smith", 22, addr2)

# Create contact manager and add contacts
manager = ContactManager()
manager.add_contact(person1)
manager.add_contact(person2)

print("=== Testing Contact Manager Save ===")
manager.save_contacts()

# Check if the file was created
import os
if os.path.exists("contacts.json"):
    print("✅ contacts.json file created successfully!")
    
    # Let's see what's in it
    with open("contacts.json", 'r') as file:
        content = file.read()
    print("\nFile contents:")
    print(content)
else:
    print("❌ No contacts.json file found")
