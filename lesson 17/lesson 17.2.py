class Author:
    def __init__(self,name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []


    def __repr__(self):
        return f"Author({self.name},{self.country},{self.birthday})"
    def __str__(self):
        return f"{self.name},({self.birthday}), {self.country}"

class Book:
    total_book = 0
    def __init__(self,name, year, author):
        self.name = name
        self.year = year
        self.author = author

    def __repr__(self):
        return f"Book({self.name}, {self.year}, {self.author})"

    def __str__(self):
        return f"{self.name}, ({self.year}) by {self.author}"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name: str, year: int, author:Author):
        book = Book(name, year, author)
        self.books.append(book)
        self.authors.append(book)
        Book.total_book += 1
        return book

    def group_by_author(self, author: Author):
        return [book for book  in self.books if book.author == author]
    def group_by_year(self, year: int):
        return [book for book in self.books if book.year == year]

    def __repr__(self):
        return f"Library ({self.name})"

    def __str__(self):
        return f"{self.name} Library"


