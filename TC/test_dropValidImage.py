from verifysitecai.Page import VerifyPage
import time
import json
from verifysitecai.Base import initilizedriver, locatorReader

browser = initilizedriver.start()


def test_locale_selection():
    file_path = "C:/Users/astham/PycharmProjects/Verifysite/verifysitecai/ConfigurationData/DSC_0011.JPG"
    r = VerifyPage.reg()

    '''r.clickOnElement(browser, "localeSelector")
    time.sleep(3)
    r.clickOnElement(browser, "locale")
'''
    #r.enterDataUsingXpathUpload(browser, "drag")

    # r.readjson(browser, "french.json")

    r.enterDataUsingXpathUpload(browser, "fileUpload", file_path)

# test_locale_selection()
