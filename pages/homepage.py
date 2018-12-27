from selenium import webdriver

class Homepage:
    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get("https://stg.veervr.tv")
        return self
