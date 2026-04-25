from utils import books

def show():
    if len(books) == 0:
        print("No books available")
    else:
        for book, quantity in books.items():
            print(f"{book} --> {quantity} copies available")