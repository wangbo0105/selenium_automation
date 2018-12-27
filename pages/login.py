from selenium import webdriver

class Login:
    def __init__(self, driver):
        self.driver = driver

    def go(self):
        self.driver.find_element_by_css_selector(".header-login").click()
        return self

    def login(self, username, password):
        self.driver.find_element_by_css_selector("#identifier").send_keys(username)
        self.driver.find_element_by_css_selector("#password").send_keys(password)
        self.driver.find_element_by_css_selector(".user-login-form .submit-btn").click()

        return self
