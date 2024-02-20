from dataclasses import dataclass, field, asdict
import json
from typing import Optional
from datetime import datetime
from google_book import GoogleBook


@dataclass()
class Book:
    id: int
    isbn: str
    title: str
    authors: list[str]
    published_Date: str
    publisher: str
    pages: int
    description: str
    webs: str
    price: tuple[float, str]
    subtitle: Optional[str] = ""
    category: Optional[str] = ""
    added_date: Optional[str] = ""
    in_stock: Optional[str] = field(default=0)

    def __post_init__(self):
        self.added_date = datetime.now().strftime("%d/%m/%Y %H:%M")


@dataclass
class Stock:
    self__books: list[Book] = field(init=False, default_factory=list[Book])

    def __post_init__(self):
        self.__books: list[Book] = self.get_Allbooks()

    def add_book(self, url, number_of_copy):

        book_data_req: GoogleBook = GoogleBook(url)
        book_data_received: dict = book_data_req.load_response()
        id: int = len(self.__books) + 1
        book = Book(id=id, **book_data_received)
        book.in_stock += number_of_copy
        if self.isExist(book.isbn):
            raise ValueError("This the book is already exist.")
        self.__books.append(book)
        self.save_books_list()
        # print(book)

    def isExist(self, isbn: str):
        for book in self.__books:
            if book.isbn == isbn:
                return True
        return False

    def list_of_books(self):
        spaceX: int = 9
        spaceY: int = 5
        print("all books that what has been added to the store")
        for book in self.__books:
            print(f'''{book.id}.  {"ISBN":<{spaceX}}{":":^{spaceY}}{book.isbn}
    {"Title":<{spaceX}}{":":^{spaceY}}{book.title}
    {"category":<{spaceX}}{":":^{spaceY}}{" ".join(book.category)}
    {"Auther":<{spaceX}}{":":^{spaceY}}{",".join(book.authors)}
    {"Publisher":<{spaceX}}{":":^{spaceY}}{book.publisher}
-----------------------------------------\n''')

    def save_books_list(self):
        with open("books.json", "w") as file:
            list_To_Json = [asdict(i) for i in self.__books]
            json.dump(list_To_Json, file, indent=4)
        print("Data has been saved successfully")
        return None

    def get_Allbooks(self) -> list[Book]:
        try:
            with open("books.json", "r", encoding="utf-8") as file:
                data: list[dict] = list(json.load(file))

            books: list[Book] = [Book(**item) for item in data]
            return books
        except Exception as e:
            print(e)
            return []

    def __str__(self):
        rstr = ''
        for i, book in enumerate(self.__books, 1):
            rstr = rstr + f'''{i}.  {"ISBN":<10}: {book.isbn:<20}
    {"Title":<10}: {book.title:<20}
    {"Auther":<10}: {",".join(book.author)}
----------------------------\n'''
        return rstr


def main():
    data = Stock()
    while True:
        try:
            url = input('Enter url: \n')
            data.add_book(url, 3)
            data.list_of_books()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
