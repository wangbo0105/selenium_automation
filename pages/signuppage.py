from pages.basepage import BasePage

class Signuppage(BasePage):
    email_input = ('css', '#identifier', 0)  #邮箱输入框
    username_input = ('css', '#fullname',0)  # 用户名输入框
    password = ('css', '#password', 0)  # 密码输入框
    signBtn = ('class', 'signup-btn', 0)  # 注册button

    def __init__(self):
        self.base = BasePage()

    def input_email(self,email):
        self.base.element.double_click(self.email_input)
        self.base.element.backSpace(self.email_input)
        """输入邮箱"""
        self.base.element.send_keys(self.email_input, email)

    def input_username(self, username):
        self.base.element.double_click(self.username_input)
        self.base.element.backSpace(self.username_input)
        """输入用户名"""
        self.base.element.send_keys(self.username_input, username)

    def input_password(self, pwd):
        self.base.element.double_click(self.password)
        self.base.element.backSpace(self.password)
        """输入密码"""
        self.base.element.send_keys(self.password, pwd)

    def submit(self):
        """点击注册button"""
        self.base.element.click(self.signBtn)

    def signup_success(self):
        self.base.element.is_element_not_exist(self.signBtn)
