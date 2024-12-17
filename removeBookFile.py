def removeBookFunction(allBooks, saveBooks):
    if allBooks:
        removeBook = int(input("Choose a book to remove : "))

        if 1 <= removeBook <= len(allBooks):
            allBooks.pop(removeBook - 1)
            saveBooks()
            print("Book successfully removed")