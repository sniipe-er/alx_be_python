class Book :
    def __init__(self, title, author, _is_checked_out):
        self.title = title
        self.author = author
        self.__is_checked_out = False

    def check_out (self):
        if not self.__is_checked_out :
            self.__is_checked_out = True
            return True
        return False
    
    def return_book (self):
        if self.__is_checked_out :
            self.__is_checked_out = False
            return True
        return False
    
    def is_available (self):
        return not self.__is_checked_out
    
class Library :
    def __init__(self,):
        self._book = []

    def add_book(self, book):
        if isinstance(book, Book):
            self._book.append(book)
            print(f"Book {book.title} by {book.author} added to the library.")
        else:
            print("Error: Only Book instances can be added.")

    def check_out_book(self, title):
        for book in self._book:
            if book.title == title and book.is_available():
                book.check_out()
                return f"'{title}' has been checked out."
        return f"'{title}' is not available."
    
    def return_book(self, title):
        for book in self._book:
            if book.title == title and not book.is_available():
                if book.return_book():
                    return f"'{title}' has been returned."
                else:
                    return f"'{title}' was not checked out."
    
    def list_available_books (self):
        available = [book for book in self._book if book.is_available()]
        if not available:
            print("No books are currently available.")
        else:
            for book in available:
                print(f"{book.title} by {book.author}")