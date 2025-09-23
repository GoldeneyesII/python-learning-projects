import json

class Serializable:
    def to_dict(self):
        result = {}
        for key, value in vars(self).items():
            if hasattr(value, 'to_dict'):
                result[key] = value.to_dict()
            else:
                try:
                    json.dumps(value) # Test serializability
                    result[key] = value
                except TypeError:
                    # Log the issue for debugging
                    # Add correct logging method at later point (only log when debug enabled)
                    print(f"Warning: {key} of type {type(value)} converted to string")
                    result[key] = str(value)
        return result

class Address(Serializable):
    def __init__(self, number, street, city, state, zipcode, street2=""):
        self.number = number
        self.street = street
        self.street2 = street2
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def __str__(self):
        lines = [f"{self.number} {self.street}"]
        if self.street2:
            lines.append(self.street2)
        lines.append(f"{self.city}, {self.state} {self.zipcode}")
        return "\n".join(lines)

class Person(Serializable):
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __str__(self):
        address_lines = str(self.address).split('\n')
        indented_address = '\n    '.join(address_lines)
        return f"{self.name}:\n  Age: {self.age}\n  Address:\n  {indented_address}\n"
    
    def show_address(self):
        message = f"{self.name}\n{self.address}"
        print(message)

    def is_older_than(self, age=25):
        return self.age > age
