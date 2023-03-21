class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald's")
book1.turn_page(50)

book2 = Book("Harry Potter", "Joanne Rowling")
book2.turn_page(100)

library = Library()
library.add_book(book1)
library.add_book(book2)

found_book = library.find_book('The Great Gatsby')
print(found_book.title)