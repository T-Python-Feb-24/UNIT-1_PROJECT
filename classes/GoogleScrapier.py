# import
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import dateutil.parser as parser
import re


class GoogleBook():
    def __init__(self, url):
        # options.add_argument
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--lang=en")
        options.add_argument("--disable-logging")
        options.add_argument("--output=/dev/null")
        options.add_argument('--log-level=3')
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_experimental_option("detach", True)

        # initilaz
        web = url
        driver = webdriver.Chrome(service=Service(), options=options)
        wait = WebDriverWait(driver=driver, timeout=10)
        driver.get(web)
        # wait until click
        try:
            price: tuple = wait.until(EC.presence_of_element_located(
                (By.XPATH, '//meta[@itemprop="price"and@content!=0]')), "No price").get_attribute("content").split("\xa0")
        except Exception as e:
            print(e)
            price = "",
        try:
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//h2[text()="About this ebook"]/parent::div/following-sibling::div/child::button'))).click()
        except Exception as e:
            print(e)
        # Extracting the ISBN of the book
        try:
            isbn: str = wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*/div[text()="ISBN"]/following-sibling::div')), "No ISBN").text
        except Exception as e:
            isbn = ""
        # Extracting the Title of the book
        title = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*/div[text()="About this ebook"]/preceding-sibling::h5'))).text
        # Extracting the description of the book
        description: str = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*/div[text()="About this ebook"]/ancestor::div[4]/child::div[2]/div/span'))).get_attribute("innerText")
        # Extracting the list of authors of the book
        authors: list[str] = [wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*/div[text()="Author"]/following-sibling::div'))).text]
        # Extracting the publisher of the book
        publisher: str = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*/div[text()="Publisher"]/following-sibling::div'))).text
        # Extracting the published date of the book
        published_Date: str = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*/div[text()="Published on"]/following-sibling::div'))).text
        pubDate = parser.parse(published_Date, default=datetime(2023, 1, 1))
        published_Date: str = datetime.date(pubDate).strftime("%d/%m/%Y")
        # Extracting the number of pages in the book
        pages: str = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*/div[text()="Pages"]/following-sibling::div'))).text
        # Extracting the categories of the book
        temp_cat: list = driver.find_elements(
            By.XPATH, '//*/div[text()="Genres"]/following-sibling::div')
        category: list[str] = list(map(lambda x: x.text, temp_cat))
        # Defining a dictionary of websites related to the book
        webs: dict = {"Amazon_Books": f'https://www.amazon.sa/s?k=isbn+{isbn}',
                      "Google_Books": web}

        new_des = []
        pattern = r'(.{' + str(80) + r'}[^\n])'
        for line in description.splitlines():
            line = re.split(pattern, line.replace(u'\xa0', u' '))
            line = [l for l in line if l]
            new_des.extend(line)
        description = "\n".join(new_des)
        self.book = {
            "isbn": isbn,
            "title": title,
            "authors": authors,
            "published_Date": published_Date,
            "publisher": publisher,
            "pages": pages,
            "description": description,
            "webs": webs,
            "price": price,
            "category": category
        }

    def get_book(self) -> dict:
        return self.book


if __name__ == '__main__':
    pass
