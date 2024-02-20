#%% 
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from datetime import date, datetime
#%%
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--lang=en")
options.add_argument('--log-level=3')
# options.add_argument("--headless")
options.add_argument("--disable-gpu")
# options.add_argument("--window-size=1920,1080")
options.add_experimental_option("detach", True)
#%%
web = input("Enter the URL of book in amazon.sa:\n")

driver = webdriver.Chrome(service=Service(), options=options)
driver.get(web)
sleep(5)
#%%
published_date = driver.find_element(
    By.XPATH, '//*[@id="detailBullets_feature_div"]/ul/li[1]/span/span[2]').text.split("(")[1][:-1]
pub_date = datetime.date(datetime.strptime(published_date,
                                           '%d %B %Y')).strftime("%d/%m/%Y")
#%%
book = {
    "isbn": driver.find_element(
        By.XPATH, '//*/span[contains(span, "ISBN-13")]/child::span[2]').text,

    "title": driver.find_element(
        By.XPATH, '//span[@id="productTitle"]').text,

    "auther": driver.find_element(
        By.XPATH, '//span[@class="author notFaded"]/child::a').text,

    "description": driver.find_element(
        By.XPATH, '//*/div[@data-feature-name="bookDescription"]/div/div/span').text,

    "publisher": driver.find_element(
        By.XPATH, '//*[@id="rpi-attribute-book_details-publisher"]/div[3]/span').text,

    "published": pub_date,

    "pages": int(driver.find_element(
        By.XPATH, '//*/span[text()="Print length"]/parent::div/following-sibling::div[2]/span').text.split(" ")[0]),

    "price": driver.find_element(
        By.XPATH, '//*/span[@id="price"]').text.split(" ")[1],

    "web": web,



}
print(book)

# //*/span[text()="Print length"]/parent::div/following-sibling::div[2]/span


# categor = driver.find_elements(
#     By.XPATH, '//span[text()="Category"]/parent::div/following-sibling::ul/li')
# print([i.text for i in categor])
# categor[1].click()

# book_element = driver.find_elements(
#     By.XPATH, '//span[text()="Category"]/parent::div/following-sibling::ul/li')
# # driver.quit()


# %%
