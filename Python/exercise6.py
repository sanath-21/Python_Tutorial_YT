# Write a Library class with no_of_books and books as two instance variables. 
# Write a program to create a library from this Library class and show how you can print all books, 
# add a book and get the number of books using different methods. 
# Show that your program doesnt persist the books after the program is stopped!

class Library:
    def __init__(self):
        Library.books=[]
        self.no_of_books = 0
    
    def addBook(self,book):
        self.books.append(book)
        self.no_of_books = len(self.books)

    def showInfo(self):
        print(f"The library has {self.no_of_books} books. The books are ")
        for book in self.books:
            print(book)
l1 = Library()
l1.addBook("Harry Potter")
l1.addBook("Harry Potter")
l1.addBook("Harry Potter")
l1.showInfo()