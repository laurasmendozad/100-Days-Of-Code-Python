''' Internet Speed Twitter Compliant Bot '''
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

PROMISED_DOWN = 100
PROMISED_UP = 50
TWITTER_USER = os.environ.get("TWITTER_USER")
TWITTER_PASSWORD = os.environ.get("TWITTER_PASSWORD")

class InternetSpeedTwitterBot:
    ''' Class with the functions required '''
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach",True)
        self.driver = webdriver.Chrome(chrome_options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        ''' Get the internet speed from scratch '''
        self.driver.get("https://www.speedtest.net/")
        sleep(2)
        self.driver.find_element(By.XPATH, '//span[text()="Go"]').click()
        sleep(60)
        self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/p[2]/button').click()
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

    def tweet_at_provider(self):
        ''' Write tweet to the internet provider '''
        self.driver.get("https://twitter.com/login")
        sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input').send_keys(TWITTER_USER)
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div').click()
        sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input').send_keys(TWITTER_PASSWORD)
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div').click()
        sleep(5)
        tweet = f"Hey @ClaroColombia, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div').send_keys(tweet)
        self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div/span/span').click()
        self.driver.quit()

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
