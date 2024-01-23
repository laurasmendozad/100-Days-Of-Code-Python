''' Challenge 2 - Use Selenium in a Blank Project & Scrape a Different Piece of Data '''
from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Main_Page")

total_articles = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
print(total_articles.text)
