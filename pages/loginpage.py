from pages.basepage import BasePage
import time


class LoginPage(BasePage):
    login_tab = ('class', 'header-login', 0)  # 导航栏-登录tab
    login_alert = ('class', 'ant-modal-content', 0)  # 登录弹窗
    username = ('id', 'loginIdentifier', 0)  # 用户名输入框
    password = ('id', 'loginPassword', 0)  # 密码输入框
    loginBtn = ('class', 'submit-btn', 0)  # 登录button
    remember = ('class', 'ant-checkbox-input', 0)  # 是否记住勾选框
    forgetPwd = ('class', 'forget-pwd', 0)  # 忘记密码
    registered = ('id', 'signupLink', 0)  # 注册
    log_out = ('link_text', '退出', 0)  # 用户tab——退出
    user_tab = ('class', 'ant-dropdown-trigger', 0)  # 用户tab
    close_login_modal = ('class', 'ant-modal-close-x', 0)  # 登录弹框关闭button
    signupLoginBtn = ('xpath', '//div[@class="tips"]/div[@class="login"]', 0)  # 注册弹框上的login button
    WeChat_button = ('id', 'wechatLoginBtn', 0)
    WeChat_modal = ('class', 'ant-modal-content', 0)
    forget_password_link = ('link_text', '忘记密码?', 0)
    forget_password_modal = ('class', 'ant-modal-body', 0)
    emailInput = ('xpath', '//div[@class="ant-modal-body"]//input', 0)
    nextStepBtn = ('xpath', '//div[@class="ant-modal-body"]//button', 0)
    explainInput = ('class', 'ant-form-explain', 0)
    emailSentModal = ('class', 'ant-modal-content', 0)
    emailSentModalClose = ('xpath', '//button[@class="ant-modal-close"]', 0)
    resentBtn = ('xpath', "//div[@class='resend']/a", 0)
    forgetPasswordClose = ('class', 'ant-modal-close', 0)

    def input_username(self, user):
        """输入用户名"""
        self.element.clear_value(self.username)
        self.element.send_keys(self.username, user)

    def input_password(self, pwd):
        """输入密码"""
        self.element.clear_value(self.password)
        self.element.send_keys(self.password, pwd)

    def click_loginBtn(self):
        """点击登录button"""
        self.element.click(self.loginBtn)

    def click_remember(self):
        """点击 记住我 勾选项"""
        self.element.click(self.remember)

    def hover_user_tab(self):
        """将鼠标移动到个人中心tab"""
        self.element.move_to_element(self.user_tab)

    def click_log_out(self):
        """点击退出tab"""
        self.element.click(self.log_out)

    def click_close_login_modal(self):
        """点击关闭登录弹框"""
        self.element.click(self.close_login_modal)

    def is_login(self):
        self.element.is_element_exist(self.user_tab)

    def is_logout(self):
        self.element.is_element_exist(self.login_tab)

    def is_login_alert(self):
        self.element.is_element_exist(self.login_alert)

    def click_signupModal_login(self):
        self.element.click(self.signupLoginBtn)

    def click_WeChat_button(self):
        self.element.click(self.WeChat_button)

    def check_WeChat_modal(self):
        self.element.is_element_exist(self.WeChat_modal)

    def click_forget_password(self):
        self.element.click(self.forget_password_link)

    def check_forget_password_modal(self):
        self.element.is_element_exist(self.forget_password_modal)

    def input_email(self, email):
        # self.element.double_click(self.emailInput)
        # self.element.backSpace(self.emailInput)
        print("email")
        print(email)
        self.element.send_keys(self.emailInput, email)

    def select_next_step(self):
        self.element.click(self.nextStepBtn)

    def check_prompt_wrong_format_email(self):
        self.element.is_element_exist(self.explainInput)

    def check_sent_email_modal(self):
        self.element.is_element_exist(self.emailSentModal)

    def close_sent_email_modal(self):
        self.element.click(self.emailSentModalClose)

    def select_resent_email(self):
        self.element.click(self.resentBtn)

    def close_forget_password_modal(self):
        self.element.click(self.forgetPasswordClose)
