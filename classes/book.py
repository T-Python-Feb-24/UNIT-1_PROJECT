from dataclasses import dataclass, field, asdict
import json
import re
from typing import Optional
from datetime import datetime

from colorama import Fore
from classes.GoogleScrapier import GoogleBook


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
    webs: dict
    price: tuple
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
        self.__books: list[Book] = self.__get_Allbooks()

    def add_book(self):
        while True:
            url: str = input(
                "Enter the URL of book in https://play.google.com/store/books/:\n")
            pattern = '^https://play.google.com/store/books/details/.*?id=.*$'
            if not re.match(pattern, url):
                print(Fore.RED+"Please enter a valid URL from Google play Book store")
                continue
            break
        while True:
            try:
                quantity = int(input("How many copies you want: "))
                break
            except Exception as e:
                print(Fore.RED + "Please enter an integer number")

        book_data_req: GoogleBook = GoogleBook(url)
        book_data_received: dict = book_data_req.get_book()
        id: int = len(self.__books) + 1
        book = Book(id=id, **book_data_received)
        book.in_stock += quantity
        if self.isExist(book.isbn):
            print("This the book is already exist but the the stock have been updated.")
        self.__books.append(book)
        self.save_books_list()

    def remove_book(self):
        self.list_of_books()
        if self.__books == []:
            return
        while True:
            try:
                book_id = int(
                    input("Put the book id to remove from the store: "))
                if book_id in range(1, len(self.__books)+1):
                    book_title: str = self.__books.pop(book_id-1).title
                    print(
                        f'{"-"*60}\nThe book ({book_title}) removed from store successfully\n{"-"*60}')
                    self.save_books_list()
                    break
                else:
                    print(
                        Fore.RED+"Wrong input you should put the book id from book list")
            except ValueError as e:
                print(e)

    def isExist(self, isbn: str):
        for book in self.__books:
            if book.isbn == isbn:
                return True
        return False

    def book_decreamnt_quantity(self, book_opject: Book):
        book: Book = self.search_book(book_opject.id)
        if book != None:
            book.in_stock -= 1

    def list_of_books(self):
        if self.__books == []:
            print("The stock is empty")
        spaceX: int = 9
        spaceY: int = 5
        print("all books that what has been added to the store")
        for book in self.__books:
            print(f'''{book.id}.  {"ISBN":<{spaceX}}{":":^{spaceY}}{book.isbn}
    {"Title":<{spaceX}}{":":^{spaceY}}{book.title}
    {"category":<{spaceX}}{":":^{spaceY}}{" ".join(book.category)}
    {"Auther":<{spaceX}}{":":^{spaceY}}{",".join(book.authors)}
    {"Publisher":<{spaceX}}{":":^{spaceY}}{book.publisher}
    {"Price":<{spaceX}}{":":^{spaceY}}{(book.price)}
-----------------------------------------\n''')

    def search_book(self, id):
        for book in self.__books:
            if book.id == id:
                return book
        print("The book id you enter was not found")

    def get_book(self, id):
        for book in self.__books:
            if book.id == id:
                return book

    def save_books_list(self):
        with open("books.json", "w") as file:
            list_To_Json = [asdict(i) for i in self.__books]
            json.dump(list_To_Json, file, indent=4)
        print("Data has been saved successfully")
        return None

    def __get_Allbooks(self) -> list[Book]:
        try:
            with open("books.json", "r", encoding="utf-8") as file:
                data: list[dict] = list(json.load(file))

            books: list[Book] = [Book(**item) for item in data]
            return books
        except Exception as e:
            print(e)
            return []

    def __len__(self) -> int:
        return len(self.__books)

    def __str__(self):
        rstr = ''
        for i, book in enumerate(self.__books, 1):
            rstr = rstr + f'''{i}.  {"ISBN":<15}: {book.isbn:<20}
    {"Title":<15}: {book.title:<20}
    {"Auther":<15}: {",".join(book.authors)}
    {"Category":<15}: {set(book.category)}
    {"Published Date":<15}: {book.published_Date}
    {"Publisher":<15}: {book.publisher}\n
    {"Description":<15}: {f"\n{"":>21}".join(book.description.splitlines())}\n
    {"webs":<15}: {f"\n{"":>21}".join(list(map(lambda i, k, v: f'{i}- {k}: {v}', range(1, len(book.webs.keys())+1), book.webs.keys(), book.webs.values())))}\n
    {"Price":<15}: {book.price[1] if len(book.price) > 1 else "The price not set yet"} {book.price[0]}
----------------------------\n'''
        return rstr


def main():
    data = Stock()
    while True:
        try:
            # url = input(
            #     "Enter the URL of book in https://play.google.com/store/books/:\n")
            # data.add_book(url, 3)
            # data.list_of_books()
            print(data)
            break
        except Exception as e:
            print(e)
            break


if __name__ == '__main__':
    main()
