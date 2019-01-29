from pages.basepage import BasePage
import time

class Signuppage(object):
    # email_input = ('id', 'identifier') #邮箱输入框
    # email_input = ('xpath', '//*[@id="identifier"]')
    email_input = ('class', 'ant-form-item', '1')    
    username_input = ('id', 'fullname')  # 用户名输入框
    password = ('id', 'password')  # 密码输入框
    signBtn = ('class', 'signup-btn')  # 登录button

    def __init__(self):
        self.base = BasePage()

    def input_email(self,email):
        time.sleep(3)
        self.base.element.double_click(self.email_input)
        self.base.element.clear(self.email_input)
        """输入邮箱"""
        self.base.element.send_keys(self.email_input, email)

    def input_username(self, username):
        self.base.element.clear(self.username_input)
        """输入用户名"""
        self.base.element.send_keys(self.username_input, username)

    def input_password(self, pwd):
        self.base.element.clear(self.password)
        """输入密码"""
        self.base.element.send_keys(self.password, pwd)

    def submit(self):
        """点击登录button"""
        self.base.element.click(self.signBtn)

    def signup_success(self):
        self.base.element.click(self.signBtn)
