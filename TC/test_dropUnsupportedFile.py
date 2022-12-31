from verifysitecai.Page import VerifyPage
import json
from verifysitecai.Base import initilizedriver, locatorReader

browser = initilizedriver.start()


def test_drop_unsupported_file():
    file_path = "C:/Users/astham/PycharmProjects/Verifysite/verifysitecai/ConfigurationData/file_example_MOV_480_700kB.mov"
    r = VerifyPage.reg()

    r.enterDataUsingXpathUpload(browser, "fileUpload", file_path)

    r.text_return(browser, "unsupported_file")







