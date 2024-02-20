# %%
import requests
import json
from datetime import datetime
# requests to google and get a response
import re


class GoogleBook:
    def __init__(self, url):

        pattern = "\\?id=([^(=|&)]+)"
        id = re.search(pattern, url)

        self.__req = requests.get(
            f"https://www.googleapis.com/books/v1/volumes?q={id.group(1)}&lang=en")
        self.__res: dict = json.loads(self.__req.text)["items"][0]
        self.__res: dict = json.loads(self.__req.text)["items"][0]
        self.__book_info: dict = self.__res["volumeInfo"]

    def load_response(self) -> dict:

        title: str = self.__book_info["title"]
        subtitle: str = self.__book_info.get("subtitle", "")
        authors: list[str] = self.__book_info["authors"]
        publisher: str = self.__book_info["publisher"]
        published_Date: str = datetime.date(datetime.strptime(self.__book_info["publishedDate"],
                                                              '%Y-%m-%d')).strftime("%d/%m/%Y")
        description: str = self.__book_info["description"]
        isbn: str = self.__book_info["industryIdentifiers"][0]["identifier"]
        pages: str = self.__book_info["pageCount"]
        category: list[str] = self.__book_info["categories"]
        price: tuple[float, str] = tuple(
            self.__res["saleInfo"]["listPrice"].values())
        webs: dict[str, str] = {
            "Google_Books": f'{self.__res["saleInfo"]["buyLink"]}',
            "Amazon_Books": f'https://www.amazon.sa/s?k=isbn+{isbn}'}
        book_dict: dict = locals()
        del book_dict["self"]
        del self.__res, self.__req, self.__book_info
        return book_dict


def main(self) -> None:
    print("in main")


if __name__ == "__main__":
    main()
