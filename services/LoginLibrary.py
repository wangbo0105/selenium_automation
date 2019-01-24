from robot.api.deco import keyword
from pages.loginpage import Loginpage
from services.CommonLibrary import CommonLibrary

    
class LoginLibrary(Loginpage):
    cl = CommonLibrary()

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
         
        self.cl.goto_page_by_click(self.login_tab)
        self.input_username(username)
        self.input_password(password)
        if not remember:
            self.click_remember()
        self.click_loginBtn()
        if expectedResult=='True':
            self.isElementExist(self.user_tab)
            self.hover_user_tab()
            self.click_log_out()
        else:
            self.click_close_login_modal()
            self.isElementExist(self.loginBtn)
