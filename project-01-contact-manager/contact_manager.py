import json
from person import Person, Address

class ContactManager:
    def __init__(self, filename="contacts.json"):
        self.filename = filename
        self.contacts = []
    
    def add_contact(self, person):
        self.contacts.append(person)
    
    def save_contacts(self):
        # Convert all Person objects to dictionaries
        contacts_data = [person.to_dict() for person in self.contacts]
        
        try:
            with open(self.filename, 'w') as file:
                json.dump(contacts_data, file, indent=2)
            print(f"Saved {len(self.contacts)} contacts to {self.filename}")
        except Exception as e:
            print(f"Error saving contacts: {e}")
    
    def load_contacts(self):
        try:
            with open(self.filename, 'r') as file:
                contacts_data = json.load(file)
               
    def load_contacts(self):
        try:
            with open(self.filename, 'r') as file:
                contacts_data = json.load(file)

            # Convert dictionaries back to Person objects
           self.contacts = [Person.from_dict(contact) for contact in contacts_data]
            print(f"Loaded {len(self.contacts)} contacts from {self.filename}")

        except FileNotFoundError:
            print(f"No existing contacts file found: {self.filename}")
            self.contacts = []
        except Exception as e:
            print(f"Error loading contacts: {e}")
            self.contacts = []
