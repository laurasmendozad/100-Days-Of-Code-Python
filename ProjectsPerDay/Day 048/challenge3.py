''' Challenge 3 - How to automate filling out forms and clicking buttons with Selenium '''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome()
driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.XPATH, '/html/body/form/input[1]')
first_name.send_keys("Laura")

last_name = driver.find_element(By.XPATH, '/html/body/form/input[2]')
last_name.send_keys("Mendoza")

email_address = driver.find_element(By.XPATH, '/html/body/form/input[3]')
email_address.send_keys("laura@email.com")

sign_up = driver.find_element(By.XPATH, '/html/body/form/button')
sign_up.send_keys(Keys.ENTER)
