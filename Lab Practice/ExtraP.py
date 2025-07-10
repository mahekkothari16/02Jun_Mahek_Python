#Library Management System
#Functions: Add book, Issue book, Return book, Show all books
#Fields: Book ID, Book Name, Author, Availability
#Extras: Use dictionary or class with file storage.

book = {}
def ask():
    book_ID = int(input("Enter the ID of the book: "))
    book_name = input("Enter the name of the book: ")
    book_author = input("Enter the author of the book: ")
    book_availability = input("Enter the availability of the book(yes/no): ").lower()
    
def add_book():
    ask1 = input("Do you want to add book(yes/no): ").lower()
    if ask1 == 'yes':
        ask()
    else:
        print('okay')


def issue_book():
    pass

def return_book():
    pass

def show_all_books():
    pass


choice = int(input("Enter the choice (1-5): "))
while True:
    if choice == 1:
        add_book()
    elif choice == 2:
        issue_book()
    elif choice == 3:
        return_book()
    elif choice == 4:
        show_all_books()
    elif choice == 5:
        break
    else:
        print("Enter valid choice.")
print("Thank you! GoodBye.")