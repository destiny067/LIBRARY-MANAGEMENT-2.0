from utils import books

def return_book():
    book_name = input("Enter book name: ").strip().upper()

    if book_name in books:
        books[book_name] += 1
        print("Book returned successfully")
    else:
        print("Book does not exist")