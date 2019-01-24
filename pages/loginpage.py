from pages.basepage import BasePage


class LoginPage(BasePage):
    login_tab = ('class', 'header-login', 0)  # 导航栏-登录tab
    login_alert = ('class', 'ant-modal-content', 0)  # 登录弹窗
    username = ('id', 'identifier', 0)  # 用户名输入框
    password = ('id', 'password', 0)  # 密码输入框
    loginBtn = ('class', 'submit-btn', 0)  # 登录button
    remember = ('class', 'ant-checkbox-input', 0)  # 是否记住勾选框
    forgetPwd = ('class', 'forget-pwd', 0)  # 忘记密码
    registered = ('id', 'signupLink', 0)  # 注册
    log_out = ('link_text', '退出', 0)  # 用户tab——退出
    user_tab = ('class', 'ant-dropdown-trigger', 0)  # 用户tab

    def input_username(self, user):
        """输入用户名"""
        self.element.send_keys(self.username, user)

    def input_password(self, pwd):
        """输入密码"""
        self.element.send_keys(self.password, pwd)

    def click_loginBtn(self):
        """点击登录button"""
        self.element.click(self.loginBtn)

    def click_remember(self):
        """点击 记住我 勾选项"""
        self.element.click(self.remember)

    def is_login(self):
        self.element.is_element_exist(self.user_tab)

    def is_logout(self):
        self.element.is_element_exist(self.login_tab)

    def is_login_alert(self):
        self.element.is_element_exist(self.login_alert)


