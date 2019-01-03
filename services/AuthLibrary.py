from selenium import webdriver
from robot.api.deco import keyword
from pages import homepage
from pages import login


class AuthLibrary:
    @keyword
    def login(self, username, password):
        driver = webdriver.Chrome()

        homepage.Homepage(driver).load()
        login_page = login.Login(driver)
        login_page.go().login(username, password)

        driver.close()
