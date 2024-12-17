def updateBookFunction(allBooks, saveBooks):
    if allBooks:
        updateBook = int(input("Choose a book to update : "))
        
        if 1 <= updateBook <= len(allBooks):
            print("1. Update title")
            print("2. Update author")
            print("3. Update price")

            updateOption = int(input("Choose an option : "))

            if updateOption == 1:
                newTitle = input("Enter new title : ")
                allBooks[updateBook - 1]["title"] = newTitle

            elif updateOption == 2:
                newAuthor = input("Enter new author : ")
                allBooks[updateBook - 1]["author"] = newAuthor

            elif updateOption == 3:
                newPrice = input("Enter new price : ")
                allBooks[updateBook - 1]["price"] = newPrice

            else:
                print("Invalid option.")

            saveBooks()
            print("Book successfully updated")