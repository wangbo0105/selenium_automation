from robot.api.deco import keyword
from pages.loginpage import Loginpage
from services.CommonLibrary import CommonLibrary


class LoginLibrary(object):

    def __init__(self):
        self.loginpage = Loginpage()
        self.cl = CommonLibrary()

    @keyword
    def login(self, username, password, remember=True):
        """登录流程
        1、点击登录tab
        2、输入用户名
        3、输入密码
        4、根据参数是否点击'记住我'
        5、点击登录button"""
        self.cl.go_page('登录')
        self.loginpage.input_username(username)
        self.loginpage.input_password(password)
        if not remember:
            self.loginpage.click_remember()
        self.loginpage.click_loginBtn()

    @keyword
    def is_login(self):
        self.loginpage.is_login()

    @keyword
    def is_logout(self):
        self.loginpage.is_logout()
