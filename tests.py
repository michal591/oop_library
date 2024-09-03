from book.models import Book
from user.models import User
from datetime import date, timedelta

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("Moby Dick", "Herman Melville")
book4 = Book("1984", "George Orwell")
book5 = Book("Pride and Prejudice", "Jane Austen")

# Create users
user1 = User("Michal", "058-3266591")
user2 = User("Ariel", "058-2222221")
user3 = User("Moti", "054-8562302")

# Loan books to users
book1.loan_book(user1)  # Loan date: 1st Oct 2024
book2.loan_book(user2)  # Loan date: 1st Oct 2024
book3.loan_book(user3)  # Loan date: 2nd Oct 2024

# Simulate returning a book
book1.return_book()  # Returned on time
book2.return_book()  # Late return
book3.loan_date = date.today() - timedelta(days=12)
book3.return_book()  # Late return
