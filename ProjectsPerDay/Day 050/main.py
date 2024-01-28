''' Auto Tinder Swiping Bot '''
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(chrome_options)
driver.get("https://tinder.com/")
sleep(2)
driver.find_element(By.XPATH, '//*[@id="c315867768"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]').click()
sleep(2)
driver.find_element(By.XPATH, '//*[@id="c537208204"]/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button').click()
sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(os.environ.get("FACEBOOK_USER"))
driver.find_element(By.XPATH, '//*[@id="pass"]').send_keys(os.environ.get("FACEBOOK_PASSWORD"))
driver.find_element(By.XPATH, '//*[@id="loginbutton"]').send_keys(Keys.ENTER)
driver.switch_to.window(base_window)
sleep(10)
driver.find_element(By.XPATH, '//*[@id="c537208204"]/main/div[1]/div/div/div[3]/button[1]').click()
driver.find_element(By.XPATH, '//*[@id="c537208204"]/main/div[1]/div/div/div[3]/button[2]').click()
driver.find_element(By.XPATH, '//*[@id="c315867768"]/div/div[2]/div/div/div[1]/div[1]/button').click()
sleep(10)
for _ in range(100):
    try:
        driver.find_element(By.XPATH, '//*[@id="c315867768"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[2]/button').click()
    except NoSuchElementException:
        sleep(5)
driver.quit()
