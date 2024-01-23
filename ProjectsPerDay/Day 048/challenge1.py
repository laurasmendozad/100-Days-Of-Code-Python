''' Challenge 1 - Use Selenium to Scrape Website Data '''
from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome()
driver.get("https://www.python.org/")

upcoming_events = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[3]/div[2]')
upcoming_events = upcoming_events.text.split("\n")
del upcoming_events[0:2]
dict_upcoming_events = {}
for i in range(int(len(upcoming_events)/2)):
    dict_upcoming_events[i] = {
        "time": upcoming_events[2*i],
        "name": upcoming_events[2*i+1]
    }
print(dict_upcoming_events)
