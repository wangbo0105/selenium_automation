from robot.api.deco import keyword
from pages.loginpage import Loginpage


class LoginLibrary(Loginpage):
    @keyword
    def login(self, username, password, remember=True):
        """登录流程
        1、点击登录tab
        2、输入用户名
        3、输入密码
        4、根据参数是否点击'记住我'
        5、点击登录button"""
        self.click_login_tab()
        self.input_username(username)
        self.input_password(password)
        if not remember:
            self.click_remember()
        self.click_loginBtn()

    @keyword
    def logout(self):
        self.hover_user_tab()
        self.click_log_out()
