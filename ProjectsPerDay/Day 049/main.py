''' Automata to Apply Jobs in LinkeIn '''
import os
import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

os.system("cls")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(chrome_options)
driver.get(
    "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=92000000"
    "&keywords=junior%20python%20developer"
    "&location=Todo%20el%20mundo"
    "&redirect=false&position=1&pageNum=0"
)
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[1]/header/nav/div/a[2]').click()
driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(os.environ.get("LINKEDIN_USER"))
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(os.environ.get("LINKEDIN_PASSWORD"))
driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button').click()
time.sleep(30)
jobs = driver.find_elements(By.CLASS_NAME,'job-card-container')
jobs = [job.text for job in jobs]
dict_jobs = {}
for job in jobs:
    dict_jobs[jobs.index(job)] = {
        'title': job.split("\n")[0],
        'company': job.split("\n")[1],
        'place': job.split("\n")[2],
        'insight': job.split("\n")[3]
    }
os.system("cls")
print(json.dumps(dict_jobs, indent=4))

filtered_jobs = {i: job_data for i, job_data in dict_jobs.items() if job_data['insight'] == "El tiempo de evaluaci\u00f3n del candidato suele ser de 1 d\u00eda"}
print(json.dumps(filtered_jobs, indent=4))

if len(filtered_jobs) != 0:
    for i, job_data in filtered_jobs.items():
        driver.find_element(By.LINK_TEXT, job_data['title']).click()
        driver.find_element(By.XPATH, "//span[text()='Solicitud sencilla']").click()
        driver.find_element(By.XPATH, "//span[text()='Enviar solicitud']").click()
else:
    print("No hay ningún trabajo con el tiempo de evaluación es mayor a un día")
