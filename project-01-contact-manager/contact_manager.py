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
                
            # TODO: Convert dictionaries back to Person objects
            # This is the next challenge!
            print(f"Loaded {len(contacts_data)} contacts from {self.filename}")
            return contacts_data
        except FileNotFoundError:
            print(f"No existing contacts file found: {self.filename}")
            return []
        except Exception as e:
            print(f"Error loading contacts: {e}")
            return []
