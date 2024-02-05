''' Instagram Follower Bot '''
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException

SIMILAR_ACCOUNT = "artoflisaking"
INSTAGRAM_USER = os.environ.get("INSTAGRAM_USER")
INSTAGRAM_PASSWORD = os.environ.get("INSTAGRAM_PASSWORD")

class InstaFollower:
    ''' Class with the functions required '''
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach",True)
        self.driver = webdriver.Chrome(chrome_options)
        self.up = 0
        self.down = 0

    def login(self):
        ''' Login to Instagram '''
        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(2)
        self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(INSTAGRAM_USER)
        self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(INSTAGRAM_PASSWORD)
        self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]/button').send_keys(Keys.ENTER)
        sleep(5)
        self.driver.find_element(By.XPATH,'//div[contains(text(),"Not now")]').click()
        sleep(5)
        self.driver.find_element(By.XPATH,'// button[contains(text(),"Not Now")]').click()

    def find_followers(self):
        ''' Find followers to the similar account '''
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers/")
        sleep(10)
        modal = self.driver.find_element(By.XPATH,'/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight",modal)
            sleep(2)

    def follow(self):
        ''' Follow the followers of the similar account '''
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value='._aano button')
        for button in all_buttons:
            try:
                button.click()
                sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(),'Cancel')]")
                cancel_button.click()
        self.driver.quit()

bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
