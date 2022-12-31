from selenium.webdriver.common.by import By
from verifysitecai.Base import locatorReader
import time
import json


class reg:

    def clickOnElement(self, driver, element):
        button = driver.find_element(By.XPATH, locatorReader.readLocator("VerifySite", element))
        # print(button)
        button.click()

    def findElementUsingClass(self, driver, element):
        button1 = driver.find_element(By.CLASS_NAME, locatorReader.readLocator("VerifySite", element))
        button1.click()

    def enterDataUsingXpath(self, driver, element):
        upload = driver.find_element(By.XPATH, locatorReader.readLocator("VerifySite", element))
        upload.click()

    def enterDataUsingXpathUpload(self, driver, element, data):
        # fpath = "C:/Users/astham/PycharmProjects/Verifysite/verifysitecai/ConfigurationData/DSC_0011.JPG"
        upload1 = driver.find_element(By.XPATH, locatorReader.readLocator("VerifySite", element))
        upload1.send_keys(data)
        time.sleep(10)

    def text_return(self, driver, element):
        a = driver.find_element(By.XPATH, locatorReader.readLocator("VerifySite", element)).text
        with open('C:/Users/astham/PycharmProjects/Verifysite/verifysitecai/ConfigurationData/french.json',
                  encoding='utf-8') as f:
            data = json.load(f)

            print(data['unsupported_file'])
            # file = json.loads(data)

        '''if "unsupported_file" in f:
            print("Key exist in JSON data")
            print("unsupported_file")
        else:
            print("Key doesn't exist in JSON data")'''
