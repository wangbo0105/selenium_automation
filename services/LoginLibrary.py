from robot.api.deco import keyword
from pages.loginpage import Loginpage
from services.CommonLibrary import CommonLibrary

    
class LoginLibrary(object):
    # cl = CommonLibrary()
    def __init__(self):
        self.cl = CommonLibrary()
        self.login = Loginpage()

    @keyword
    def login(self, username, password, expectedResult, remember=True):

        """登录流程
        1、点击登录tab
        2、输入用户名
        3、输入密码
        4、根据参数是否点击'记住我'
        5、点击登录button
        6.判断登录成功&失败
        7.退出登录"""      
         
        self.login.click_login()
        # cl.goto_page_by_click(self.login_tab)
        self.login.input_username(username)
        self.login.input_password(password)
        if not remember:
            self.login.click_remember()
        self.click_loginBtn()
        if expectedResult=='True':
            self.login.isElementExist(self.user_tab)
            self.login.hover_user_tab()
            self.login.click_log_out()
        else:
            self.login.click_close_login_modal()
            self.login.isElementExist(self.loginBtn)
