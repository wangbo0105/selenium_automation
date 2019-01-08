from Base.base import Base


class Loginpage(Base):
    login_tab = ('class', 'header-login')  # 登录tab
    username = ('id', 'identifier')  # 用户名输入框
    password = ('id', 'password')  # 密码输入框
    loginBtn = ('class', 'submit-btn')  # 登录button
    remember = ('class', 'ant-checkbox-input')  # 是否记住勾选框
    forgetPwd = ('class', 'forget-pwd')  # 忘记密码
    registered = ('id', 'signupLink')  # 注册
    log_out = ('link_text', '退出')  # 用户tab——退出
    user_tab = ('class', 'ant-dropdown-trigger')  # 用户tab

    # def click_login_tab(self):
    #     """点击login tab"""
    #     self.click(self.findElement(self.login_tab))

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

    # def hover_user_tab(self):
    #     """将鼠标移动到个人中心tab"""
    #     self.move_to_element(self.findElement(self.user_tab))
    #     time.sleep(3)
    #
    # def click_log_out(self):
    #     """点击退出tab"""
    #     self.click(self.findElement(self.log_out))


