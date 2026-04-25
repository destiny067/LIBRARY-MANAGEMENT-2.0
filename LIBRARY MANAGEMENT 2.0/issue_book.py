from utils import books

def issue():
    book_name = input("Enter book name: ").strip().upper()

    if book_name in books:
        if books[book_name] > 0:
            books[book_name] -= 1
            print("Book issued successfully")
        else:
            print("No copies available")
    else:
        print("Book not found")