''' Data Entry Job Automation '''
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests

URL = "https://appbrewery.github.io/Zillow-Clone/"

response = requests.get(URL, timeout=10)
soup = BeautifulSoup(response.text, "html.parser")
addresses = soup.find_all('address',{'data-test':'property-card-addr'})
addresses = [address.get_text().strip() for address in addresses]
prices = soup.find_all('span',{'data-test':'property-card-price'})
prices = [price.get_text().strip().split('/')[0].split('+')[0] for price in prices]
links = soup.find_all('a',{'data-test':'property-card-link','tabindex':'-1'})
links = [link.get('href') for link in links]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(chrome_options)
driver.get("https://forms.gle/Hpp3LwcaKxeyrCa5A")
sleep(2)
for i in range(len(addresses)):
    driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(addresses[i])
    driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(prices[i])
    driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(links[i])
    driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()
    sleep(1)
    driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()
driver.quit()
