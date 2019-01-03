from services.BrowserLibrary import BrowserLibrary
import time


class Loginpage(BrowserLibrary):
    login_tab = ('class', 'header-login')  # 登录tab
    username = ('id', 'identifier')  # 用户名输入框
    password = ('id', 'password')  # 密码输入框
    loginBtn = ('class', 'submit-btn')  # 登录button
    remember = ('class', 'ant-checkbox-input')  # 是否记住勾选框
    forgetPwd = ('class', 'forget-pwd')  # 忘记密码
    registered = ('id', 'signupLink')  # 注册
    log_out = ('link_text', '退出')  # 用户tab——退出
    user_tab = ('xpath', '//*[@id="app"]/div/div/header/nav[1]/div/div[2]/a/div[2]')  # 用户tab

    def click_login_tab(self):
        """点击login tab"""
        login_tab = self.base.findElement(self.login_tab)
        self.base.click(login_tab)

    def input_username(self, user):
        """输入用户名"""
        username = self.base.findElement(self.username)
        self.base.send_keys(username, user)

    def input_password(self, pwd):
        """输入密码"""
        password = self.base.findElement(self.password)
        self.base.send_keys(password, pwd)

    def click_loginBtn(self):
        """点击登录button"""
        login_button = self.base.findElement(self.loginBtn)
        self.base.click(login_button)

    def click_remember(self):
        """点击 记住我 勾选项"""
        remember = self.base.findElement(self.remember)
        self.base.click(remember)

    def hover_user_tab(self):
        """将鼠标移动到个人中心tab"""
        mine = self.base.findElement(self.user_tab)
        self.base.move_to_element(mine)
        time.sleep(3)

    def click_log_out(self):
        """点击退出tab"""
        log_out = self.base.findElement(self.log_out)
        self.base.click(log_out)


