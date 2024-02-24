import json
from datetime import date 
from colorama import Fore, Back, Style
class Library:
    def __init__(self) -> None:
        self.__list_of_books = self.read_books_file()

    def get_list_of_book(self):
        return self.__list_of_books
    
    def read_books_file(self):
        try:
            with open('books.json', mode='r', encoding='utf-8') as file:
                list_of_books = json.loads(file.read())
                return list_of_books
        except FileNotFoundError:
            return []
    
    def save_books_file(self, list_of_books):
        with open('books.json', mode='w', encoding='utf-8') as file:
            books_file_contents = json.dumps(list_of_books)
            file.write(books_file_contents)
    
    def add_book(self, list_of_books):
        print('Here you can add your new book!')
        id: str = input('Please enter book id: ')
        title:str = input("Please enter the title of the new book: ")
        author:str = input('Please enter the author name: ')
        published:date = input('Please enter the date of published(YYYY-MM-DD): ')
        pages:int = int(input('Please enter the number of pages: '))
        description:str = input('Please enter the description of the book: ')
        availability:int = int(input('Please enter the quantity you have: '))
        new_book:dict = {
            'id':id,
            'title':title,
            'author':author,
            'published':published,
            'pages':pages,
            'description':description,
            'availability':availability
        }
        self.__list_of_books.append(new_book)
        self.save_books_file(self.__list_of_books)
        print(Fore.GREEN+'Book Added Successfully')
        print(Style.RESET_ALL)

        


