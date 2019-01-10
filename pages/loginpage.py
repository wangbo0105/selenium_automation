from pages.basepage import BasePage


class Loginpage(BasePage):
    login_tab = ('class', 'header-login')  # 导航栏-登录tab
    username = ('id', 'identifier')  # 用户名输入框
    password = ('id', 'password')  # 密码输入框
    loginBtn = ('class', 'submit-btn')  # 登录button
    remember = ('class', 'ant-checkbox-input')  # 是否记住勾选框
    forgetPwd = ('class', 'forget-pwd')  # 忘记密码
    registered = ('id', 'signupLink')  # 注册
    log_out = ('link_text', '退出')  # 用户tab——退出
    user_tab = ('class', 'ant-dropdown-trigger')  # 用户tab

    def input_username(self, user):
        """输入用户名"""
        self.send_keys(self.findElement(self.username), user)

    def input_password(self, pwd):
        """输入密码"""
        self.send_keys(self.findElement(self.password), pwd)

    def click_loginBtn(self):
        """点击登录button"""
        self.click(self.findElement(self.loginBtn))

    def click_remember(self):
        """点击 记住我 勾选项"""
        self.click(self.findElement(self.remember))


