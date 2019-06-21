from pages.basepage import BasePage
import time


class SignupPage(BasePage):
    signupBtn = ('xpath', '//div[@class="login-options"]//a', 0)
    email_input = ('css', '#signupIdentifier', 0)  # 邮箱输入框
    email_type = ('xpath', '//div[@class="signup-options"]/div', 1)

    username_input = ('css', '#signupUsername', 0)  # 用户名输入框
    nickname_input = ('css', '#signupFullname', 0)
    fullname_input = ('css', '#signupFullname', 0)  
    password = ('css', '#signupPassword', 0)  # 密码输入框
    signBtn = ('css', '.ant-btn.ant-btn-primary.ant-btn-lg.submit-btn', 0)  # 注册button
    # signBtn = ('xpath', '/html/body/div[6]/div/div[2]/div/div[1]/div/div[3]/form/button', 0)  # 注册button
    
    signupModalCloseBtn = ('class', 'ant-modal-close', 0)

    purposeModal = ('class', 'ant-modal-content', 0)
    purposeModalSkipBtn = ('css', '.skip-btn', 0)
    purposeItem = ('class', 'list-item', 0)
    purposeModalDone = ('xpath', "//div[@class='purpose-modal-btns']/button", 0)
    purposeModalCloseBtn = ('class', 'ant-modal-close', 0)
    explain_is_exit = ('class', 'ant-form-explain', 0)

    def clickSignupButton(self):
        self.element.click(self.signupBtn)

    def select_email(self):
        self.element.click(self.email_type)

    def input_email(self, email):
        self.element.double_click(self.email_input)
        self.element.backSpace(self.email_input)
        """输入邮箱"""
        self.element.send_keys(self.email_input, email)

    def input_username(self, username):
        self.element.double_click(self.username_input)
        self.element.backSpace(self.username_input)
        """输入用户名"""
        self.element.send_keys(self.username_input, username)

    def input_nickname(self, nickname):
        self.element.double_click(self.nickname_input)
        self.element.backSpace(self.nickname_input)
        """输入昵称"""
        self.element.send_keys(self.nickname_input, nickname)

    def input_fullname(self, fullname):
        self.element.double_click(self.fullname_input)
        self.element.backSpace(self.fullname_input)
        """输入昵称"""
        self.element.send_keys(self.fullname_input, fullname)

    def input_password(self, pwd):
        self.element.double_click(self.password)
        self.element.backSpace(self.password)
        """输入密码"""
        self.element.send_keys(self.password, pwd)

    def submit(self):
        """点击注册button"""
        self.element.click(self.signBtn)
        time.sleep(3)

    def signup_success(self):
        self.element.is_element_not_exist(self.email_input)

    # def is_exist_purposeModal(self):
    #     self.element.is_element_exist(self.purposeModal)

    # def skip_purposeModal(self):
    #     self.element.click(self.purposeModalSkipBtn)

    # def click_purposeModalCloseBtn(self):
    #     self.element.click(self.purposeModalCloseBtn)

    # def is_exist_signupModal(self):
    #     self.element.is_element_exist(self.signupModalCloseBtn)

    # def click_signupModalClose(self):
    #     self.element.click(self.signupModalCloseBtn)

    # def click_one_purpose(self):
    #     self.element.click(self.purposeItem)

    # def cancel_click_one_purpose(self):
    #     self.element.click(self.purposeItem)

    # def one_purpose_is_selected(self):
    #     active = self.element.get_attribute(self.purposeItem, 'class')
    #     self.element.should_contains(active, 'active')

    # def one_purpose_is_not_selected(self):
    #     active = self.element.get_attribute(self.purposeItem, 'class')
    #     self.element.should_be_equal(active, 'list-item')

    # def done_purposeModal(self):
    #     self.element.click(self.purposeModalDone)

    # def explain_is_email_registered(self):
    #     self.element.is_element_exist(self.explain_is_exit)

    # def explain_is_please_enter_email(self):
    #     self.element.is_element_exist(self.explain_is_exit)

    # def explain_is_please_enter_password(self):
    #     self.element.is_element_exist(self.explain_is_exit)

    # def check_prompt_is_password_less_6_characters(self):
    #     self.element.is_element_exist(self.explain_is_exit)
                                                                                     