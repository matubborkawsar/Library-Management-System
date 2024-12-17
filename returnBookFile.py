def returnBookFunction(allBooks, saveBooks, allBorrowers, saveBorrowers):
    if allBooks:
        returnBook = int(input("Choose a book to return : "))

        phone = input("Enter borrower's phone : ")

        for borrower in allBorrowers:
            if phone == borrower['phone']:
                if borrower['borrowed'] > 0:
                    borrower['borrowed'] = borrower['borrowed'] - 1
                    saveBorrowers()
                else: 
                    print("Borrower didn't borrow any books")

        if 0 < returnBook <= len(allBooks):
            allBooks[returnBook - 1]["quantity"] = allBooks[returnBook - 1]["quantity"] + 1
            saveBooks()
            print("Book successfully returned")
        else:
            print("Invalid option.")