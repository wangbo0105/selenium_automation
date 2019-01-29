from robot.api.deco import keyword
from pages.loginpage import LoginPage
from services.CommonLibrary import CommonLibrary


class LoginLibrary(object):

    def __init__(self):
        self.loginpage = LoginPage()
        self.common = CommonLibrary()

    @keyword
    def all_login(self, username, password, expectedResult, remember=True):

        """登录流程
        1、点击登录tab
        2、输入用户名
        3、输入密码
        4、根据参数是否点击'记住我'
        5、点击登录button
        6.判断登录成功&失败
        7.退出登录"""

        self.common.go_page('login')
        self.loginpage.input_username(username)
        self.loginpage.input_password(password)
        if not remember:
            self.loginpage.click_remember()
        self.loginpage.click_loginBtn()
        if expectedResult == 'True':
            self.loginpage.element.is_element_exist(self.loginpage.user_tab)
            self.loginpage.hover_user_tab()
            self.loginpage.click_log_out()
        else:
            self.loginpage.click_close_login_modal()
            self.loginpage.element.is_element_exist(self.loginpage.login_tab)

    @keyword
    def login(self, username, password, remember=True):
        self.common.go_page('login')
        self.loginpage.input_username(username)
        self.loginpage.input_password(password)
        if not remember:
            self.loginpage.click_remember()
        self.loginpage.click_loginBtn()

    @keyword
    def log_out(self):
        self.loginpage.click_log_out()

    @keyword
    def check_the_login_alert_is_displayed(self):
        self.loginpage.is_login_alert()

    @keyword
    def check_you_are_logged_in(self):
        self.loginpage.is_login()

    @keyword
    def check_you_are_logged_out(self):
        self.loginpage.is_logout()
