from selenium import webdriver
from robot.api.deco import keyword


class BootstrapLibrary:
    @keyword
    def goto_baidu(self):
        driver = webdriver.Chrome()
        driver.get("https://baidu.com")
        driver.close()
