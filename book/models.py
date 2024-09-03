"""
Library models:
book model.
Attributes: Name, author, user
Methods: __init__, __str__, loan_book(user), return_book()
User model:
Attributes: Name, phone number
Methods: __init__,__str__
Make a list of 5 books and 3 users
Loan 3 books by 3 different users (in tests.py file)
Add a date field for user and user can loan up to 10 days. 
When a user loans - print the return date
If the user is late - print: “YOU ARE LATE. The fine is 50 shekel”
"""

from datetime import timedelta, date


class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author
        self.user = None
        self.loan_date = date.today()

    def __str__(self):
        return f"Book:{self.name}- Author:{self.author}"

    def loan_book(self, user):
        self.user = user
        print(
            f"The book '{self.name}' is borrowed by {self.user.name}. Date: {self.loan_date}"
        )

    def return_book(self):
        return_date = date.today()
        if return_date > self.loan_date + timedelta(days=10):
            print(f"{self.name}- YOU ARE LATE. The fine is 50 shekel")
        else:
            print(f"{self.name}-Book returned on time. Thank you!")
        self.user = None
        self.loan_date = None
