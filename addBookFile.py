import random
import datetime

def addBookFunction(allBooks, saveBooks):
    title = input("Enter book title : ")
    author = input("Enter author name : ")
    price = input("Enter unit price : ")
    quantity = int(input("Enter book quantity : "))

    isbn = random.randint(1000, 9999)
    createAt = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    book = {
        'isbn': isbn,
        'title': title,
        'author': author,
        'price': price,
        'quantity': quantity,
        'createAt': createAt
    }
    allBooks.append(book)
    saveBooks()

    print("Book successfully added")