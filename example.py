from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
import configparser

driver = webdriver.Chrome()

print('enter locale code: ')
a = input()
if a == "de":
    driver.get("https://verify.contentauthenticity.org/inspect?lang=de")
elif a == 'fr':
    driver.get("https://verify.contentauthenticity.org/inspect?lang=fr")
elif a == 'jp':
    driver.get("https://verify.contentauthenticity.org/inspect?lang=jp")
else:
    driver.get("https://verify.contentauthenticity.org/inspect")

driver.maximize_window()
time.sleep(5)

button = driver.find_element(By.XPATH, "//input[@data-test-id='viewer.fileInput']")
print(button)
button.send_keys("C:/Users/astham/PycharmProjects/Verifysite/verifysitecai/ConfigurationData/DSC_0011.JPG")
time.sleep(10)
print("Executed")

with open('C:/Users/astham/PycharmProjects/Verifysite/verifysitecai/ConfigurationData/french.json') as f:
    data = json.load(f)

print(data)
