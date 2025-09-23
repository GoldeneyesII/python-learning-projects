# Import your classes (assuming they're in person.py)
from person import Person, Address

# Test 1: Create addresses with and without street2
print("\n=== Testing Address Class ===")

# Address without apartment/suite
addr1 = Address("123", "Main St", "Spokane", "WA", "99201")
print("Address 1 (no apt):")
print(addr1)
print()

# Address with apartment/suite
addr2 = Address("456", "Pine Ave", "Seattle", "WA", "98101", "Apt 4B")
print("Address 2 (with apt):")
print(addr2)
print()

# Test 2: Create people and test methods
print("\n=== Testing Person Class ===")

person1 = Person("John Doe", 31, addr1)
person2 = Person("Jane Smith", 22, addr2)

print("Person 1:")
print(person1)

print("Person 2:")
print(person2)

# Test 3: Test the is_older_than method
print("\n=== Testing Age Methods ===")
print(f"Is {person1.name} older than 25? {person1.is_older_than()}")
print(f"Is {person2.name} older than 25? {person2.is_older_than()}")
print(f"Is {person1.name} older than 35? {person1.is_older_than(35)}")

# Test 4: Test show_address method
print("\n=== Testing Show Address Method ===")
person1.show_address()

# Add this to your test_person.py file
print("\n=== Testing Serialization ===")

# Create test objects
addr1 = Address("123", "Main St", "Spokane", "WA", "99201")
person1 = Person("John Doe", 31, addr1)

# Test to_dict
person_dict = person1.to_dict()
print("Person as dictionary:")
print(person_dict)
print()

# Test JSON serialization
import json
try:
    person_json = json.dumps(person_dict, indent=2)
    print("Person as JSON:")
    print(person_json)
    print()
except Exception as e:
    print(f"JSON serialization failed: {e}")

# Test with a problematic object (to see the fallback in action)
import datetime
person1.birthday = datetime.date(1992, 5, 15)  # Add a date object
person_dict_with_date = person1.to_dict()
print("Person with date object:")
print(person_dict_with_date)
