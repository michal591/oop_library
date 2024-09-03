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

from datetime import timedelta


class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def __str__(self):
        return f"Book:{self.name}- Author:{self.author}"

    def loan_book(self, user, loan_date):
        self.user = user
        self.loan_date = loan_date
        self.return_date = loan_date + timedelta(days=10)
        print(
            f"The book '{self.name}' is borrowed by {self.user.name}. Date to return: {self.return_date}"
        )

    def return_book(self, return_date):
        if return_date > self.return_date:
            print(f"{self.name}- YOU ARE LATE. The fine is 50 shekel")
        else:
            print(f"{self.name}-Book returned on time. Thank you!")
        # Clear the loan details
        self.user = None
        self.loan_date = None
        self.return_date = None
