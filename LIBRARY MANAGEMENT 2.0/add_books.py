from utils import books

def add():
    book_name = input("Enter book name: ").strip().upper()
    quantity = int(input("Enter number of books: "))

    if book_name in books:
        books[book_name] += quantity
        print(f"{quantity} more books added")
    else:
        books[book_name] = quantity
        print("Book added successfully")