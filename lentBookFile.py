def lendBookFunction(allBooks, saveBooks, allBorrowers, saveBorrowers):
    if allBooks:
        lendBook = int(input("Choose a book to lend : "))

        print("1. Existing borrower")
        print("2. New borrower")
        
        borrowerType = int(input("Enter borrower type : "))

        if borrowerType == 1:
            phone = input("Enter borrower phone : ")

            for borrower in allBorrowers:
                if phone == borrower['phone']:
                    if borrower['borrowed'] < 5:
                        borrower['borrowed'] = borrower['borrowed'] + 1
                        saveBorrowers()
                    else: 
                        print("Borrower borrows a maximum book")

        elif borrowerType == 2:
            name = input("Enter borrower name : ")
            phone = input("Enter borrower phone : ")

            if 0 < lendBook <= len(allBooks):
                if allBooks[lendBook - 1]["quantity"] > 0:
                    allBooks[lendBook - 1]["quantity"] = allBooks[lendBook - 1]["quantity"] - 1
                    saveBooks()
                    print("Book successfully lent")
                else:
                    print("Book quantity 0")
            else:
                print("Invalid option.")

            borrower = {
                'name': name,
                'phone': phone,
                'book': allBooks[lendBook - 1]['title'],
                'borrowed': 1
            }

            allBorrowers.append(borrower)
            saveBorrowers()