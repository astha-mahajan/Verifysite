from selenium import webdriver

''' from selenium.webdriver.common.by import By '''
import time

driver = webdriver.Chrome()


def start():
   # response = webdriver.request('POST', 'url here', data={"param1": "value1"})
    driver.get("https://verify.contentauthenticity.org/inspect?lang=fr")
    driver.maximize_window()
    time.sleep(5)
    return driver

def stop():
    driver.close()
