"""
Attributes: Name, phone number
Methods: __init__,__str__
"""


class User:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    def __str__(self):
        return f"user: {self.name}- {self.phone_number}"
