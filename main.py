import json

import addBookFile, removeBookFile, updateBookFile, lentBookFile, returnBookFile

print("Welcome")

allBooks = []


try:
    with open("allBooks.json", "r") as allBooksFile:
        allBooks = json.load(allBooksFile)
except:
    allBooks = []


def saveBooks():
    with open("allBooks.json", "w") as allBooksFile:
        json.dump(allBooks, allBooksFile, indent=4)

def viewBooks():
    if allBooks:
        for index, book in enumerate(allBooks):
            print(f"{index + 1}. ISBN: {book['isbn']}, Title: {book['title']}, Author: {book['author']}, Price: {book['price']}, Quantity: {book['quantity']}, Create at: {book['createAt']}")
    else:
        print("No book found")

allBorrowers = []

try:
    with open("allBorrowers.json", "r") as allBorrowersFile:
        allBorrowers = json.load(allBorrowersFile)
except:
    allBorrowers = []

def saveBorrowers():
    with open("allBorrowers.json", "w") as allBorrowersFile:
        json.dump(allBorrowers, allBorrowersFile, indent=4)

def viewBorrowers():
    if allBorrowers:
        for index, borrower in enumerate(allBorrowers):
            print(f"{index + 1}. Name: {borrower['name']}, Phone: {borrower['phone']}, Borrowed: {borrower['borrowed']}")
    else:
        print("No borrower found")

while True:
    print(f"\n1. Add a book")
    print("2. Remove a book")
    print("3. Update a book")
    print("4. View all books")
    print("5. Lend a book")
    print("6. Return a book")
    print("7. View all borrowers")
    print("0. Exit")



    option = int(input("Choose an option : "))



    if option == 1:
        addBookFile.addBookFunction(allBooks, saveBooks)

    elif option == 2:
        viewBooks()

        removeBookFile.removeBookFunction(allBooks, saveBooks)
        
    elif option == 3:
        viewBooks()

        updateBookFile.updateBookFunction(allBooks, saveBooks)
        
    elif option == 4:
        viewBooks()

    elif option == 5:
        viewBooks()

        lentBookFile.lendBookFunction(allBooks, saveBooks, allBorrowers, saveBorrowers)
        
    elif option == 6:
        viewBooks()

        returnBookFile.returnBookFunction(allBooks, saveBooks, allBorrowers, saveBorrowers)

    elif option == 7:
        viewBorrowers()

    elif option == 0:
        print("Thank you.")
        break

    else:
        print("Invalid option. Try 1,2,3,4 or 0")