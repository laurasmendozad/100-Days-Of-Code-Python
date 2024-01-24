''' Cookie Clicker Bot '''
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.XPATH, '//*[@id="cookie"]')
store = driver.find_element(By.XPATH,'//*[@id="store"]').text.split("\n")
store = [store[2*i].split(" - ")[0] for i in range(int(len(store)/2))]
timeout_5min = time.time() + 5*60
while time.time() < timeout_5min:
    timeout_5s = time.time() + 5
    while time.time() < timeout_5s:
        cookie.click()

    money = int(driver.find_element(By.XPATH,'//*[@id="money"]').text.replace(",",""))
    dict_store = {}
    for index, name in enumerate(store):
        value = driver.find_element(By.XPATH,f'//*[@id="buy{name}"]/b').text.split('-')[1].strip()
        dict_store[name] = int(value.replace(",",""))

    for n, v in reversed(dict_store.items()):
        if money > v:
            element = driver.find_element(By.XPATH, f'//*[@id="buy{n}"]')
            element.click()
            break

print(driver.find_element(By.XPATH,'//*[@id="cps"]').text)
