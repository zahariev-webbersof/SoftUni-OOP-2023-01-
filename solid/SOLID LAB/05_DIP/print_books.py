from abc import ABC, abstractmethod

class Book:
    def __init__(self, content: str):
        self.content = content

class IFormatter(ABC):
    @abstractmethod
    def format(self, book: Book) -> str:
        pass

class Formatter:
    def format(self, book: Book) -> str:
        return book.content

class IPrinter(ABC):
    @abstractmethod
    def get_book(self, book: Book) -> str:
        pass

class Printer:
    def __init__(self, formatter: IFormatter):
        self.formatter = formatter

    def get_book(self, book: Book):
        formatter = Formatter()
        formatted_book = formatter.format(book)
        return formatted_book


book = Book('This is the content of the book')
formatter = Formatter()
printer = Printer(formatter)

formatted_book = printer.get_book(book)
print(formatted_book)