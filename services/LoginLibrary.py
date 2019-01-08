from robot.api.deco import keyword
from pages.loginpage import Loginpage
from services.CommonLibrary import CommonLibrary


class LoginLibrary(Loginpage):
    cl = CommonLibrary()

    @keyword
    def login(self, username, password, remember=True):
        """登录流程
        1、点击登录tab
        2、输入用户名
        3、输入密码
        4、根据参数是否点击'记住我'
        5、点击登录button"""
        self.cl.goto_page_by_click(self.login_tab)
        self.input_username(username)
        self.input_password(password)
        if not remember:
            self.click_remember()
        self.click_loginBtn()

    @keyword
    def logout(self):
        self.cl.goto_page_by_hover(self.user_tab, self.log_out)

    @keyword
    def is_login(self):
        self.isElementExist(self.user_tab)

    @keyword
    def is_logout(self):
        self.isElementExist(self.login_tab)
