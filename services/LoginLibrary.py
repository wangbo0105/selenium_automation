from robot.api.deco import keyword
from pages.loginpage import LoginPage
from services.CommonLibrary import CommonLibrary
from pages.basepage import BasePage
import time


class LoginLibrary(object):

    def __init__(self):
        self.loginpage = LoginPage()
        self.common = CommonLibrary()
        self.base = BasePage()

    @keyword
    def all_login(self, username=None, password=None, expectedResult=True, remember=True):

        """登录流程
        1、点击登录tab
        2、输入用户名
        3、输入密码
        4、根据参数是否点击'记住我'
        5、点击登录button
        6.判断登录成功&失败
        7.退出登录"""

        self.common.go_page('login')
        # time.sleep(3)
        self.loginpage.input_username(username)
        self.loginpage.input_password(password)
        time.sleep(3)
        if not remember:
            self.loginpage.click_remember()
        self.loginpage.click_loginBtn()

        # if expectedResult == "True":
        if expectedResult:
            self.loginpage.is_login()
            time.sleep(3)
            self.loginpage.hover_user_tab()
            self.loginpage.click_log_out()

        else:
        # if expectedResult == "False":   
            self.loginpage.click_close_login_modal()
            self.base.element.is_element_exist(self.loginpage.login_tab)

    # def sign_up(self, email =None , username =None, password = None,ExpectedResult = True):
    #         self.signup.input_email(email)
    #         self.signup.input_username(username)
    #         self.signup.input_password(password)
    #         self.signup.submit()
    #         if ExpectedResult == 'False':
    #           self.close_signup_modal()

    @keyword
    def login(self, username, password, remember=True):
        self.common.go_page('login')
        self.loginpage.input_username(username)
        self.loginpage.input_password(password)
        if not remember:
            self.loginpage.click_remember()
        self.loginpage.click_loginBtn()
        time.sleep(3)

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

    # @keyword
    # def select_login(self):
    #     self.loginpage.click_signupModal_login()

    @keyword
    def select_WeChat(self):
        self.loginpage.click_WeChat_button()

    @keyword
    def check_WeChat_modal(self):
        self.loginpage.check_WeChat_modal()

    @keyword
    def select_forget_password(self):
        self.loginpage.click_forget_password()

    @keyword
    def check_forget_password_modal(self):
        self.loginpage.check_forget_password_modal()

    @keyword
    def input_email(self, email):
        self.loginpage.input_email(email)
        print("hello word")
        print(email)

    @keyword
    def select_next_step(self):
        self.loginpage.select_next_step()

    @keyword
    def check_prompt_wrong_format_email(self):
        self.loginpage.check_prompt_wrong_format_email()

    @keyword
    def check_sent_email_modal(self):
        self.loginpage.check_sent_email_modal()

    @keyword
    def close_sent_email_modal(self):
        self.loginpage.close_sent_email_modal()

    @keyword
    def select_resent_email(self):
        self.loginpage.select_resent_email()

    @keyword
    def close_forget_password_modal(self):
        self.loginpage.close_forget_password_modal()

    @keyword
    def close_login_modal(self):
        self.loginpage.click_close_login_modal()
    

    @keyword
    def free_login(self, username, password):
        self.login(username, password)
        self.base.browser.get_cookies()
        self.base.browser.add_cookies()
