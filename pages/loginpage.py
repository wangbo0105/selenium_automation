from pages.basepage import BasePage

class LoginPage(object):
    login_tab = ('class', 'header-login', 0)  # 导航栏-登录tab
    login_alert = ('class', 'ant-modal-content', 0)  # 登录弹窗
    username = ('css', '#identifier', 0)  # 用户名输入框
    password = ('css', '#password', 0)  # 密码输入框
    loginBtn = ('class', 'submit-btn', 0)  # 登录button
    remember = ('class', 'ant-checkbox-input', 0)  # 是否记住勾选框
    forgetPwd = ('class', 'forget-pwd', 0)  # 忘记密码
    registered = ('id', 'signupLink', 0)  # 注册
    log_out = ('link_text', '退出', 0)  # 用户tab——退出
    user_tab = ('class', 'ant-dropdown-trigger', 0)  # 用户tab
    close_login_modal = ('class', 'ant-modal-close', 0)  # 登录弹框关闭button

    def __init__(self):
        self.base = BasePage()

    def input_username(self, user):
        """输入用户名"""
        # self.base.element.clear(self.username)

        self.base.element.double_click(self.username)
        self.base.element.backSpace(self.username)
        self.base.element.send_keys(self.username, user)

    def input_password(self, pwd):
        """输入密码"""
        self.base.element.double_click(self.password)
        self.base.element.backSpace(self.password)
        self.base.element.send_keys(self.password, pwd)

    def click_loginBtn(self):
        """点击登录button"""
        self.base.element.click(self.loginBtn)

    def click_remember(self):
        """点击 记住我 勾选项"""
        self.base.element.click(self.remember)

    def hover_user_tab(self):
        """将鼠标移动到个人中心tab"""
        self.base.element.move_to_element(self.user_tab)

    def click_log_out(self):
        """点击退出tab"""
        self.base.element.click(self.log_out)

    def click_close_login_modal(self):
        """点击关闭登录弹框"""
        self.base.element.click(self.close_login_modal)

    def is_login(self):
        self.base.element.is_element_exist(self.user_tab)

    def is_logout(self):
        self.base.element.is_element_exist(self.login_tab)

    def is_login_alert(self):
        self.base.element.is_element_exist(self.login_alert)
