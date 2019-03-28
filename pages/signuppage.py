from pages.basepage import BasePage


class SignupPage(BasePage):
    email_input = ('css', '#identifier', 0)  # 邮箱输入框
    username_input = ('css', '#fullname', 0)  # 用户名输入框
    password = ('css', '#password', 0)  # 密码输入框
    signBtn = ('class', 'signup-btn', 0)  # 注册button
    signupModalCloseBtn = ('class', 'ant-modal-close', 0)

    purposeModal = ('class', 'ant-modal-content', 0)
    purposeModalSkipBtn = ('css', '.skip-btn', 0)
    purposeItem = ('class', 'list-item', 0)
    purposeModalDone = ('xpath', "//div[@class='purpose-modal-btns']/button", 0)
    purposeModalCloseBtn = ('class', 'ant-modal-close', 0)
    explain_is_exit = ('class', 'ant-form-explain', 0)

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

    def input_password(self, pwd):
        self.element.double_click(self.password)
        self.element.backSpace(self.password)
        """输入密码"""
        self.element.send_keys(self.password, pwd)

    def submit(self):
        """点击注册button"""
        self.element.click(self.signBtn)

    def signup_success(self):
        self.element.is_element_not_exist(self.signBtn)

    def is_exist_purposeModal(self):
        self.element.is_element_exist(self.purposeModal)

    def skip_purposeModal(self):
        self.element.click(self.purposeModalSkipBtn)

    def click_purposeModalCloseBtn(self):
        self.element.click(self.purposeModalCloseBtn)

    def is_exist_signupModal(self):
        self.element.is_element_exist(self.signupModalCloseBtn)

    def click_signupModalClose(self):
        self.element.click(self.signupModalCloseBtn) 

    def click_one_purpose(self):
        self.element.click(self.purposeItem)
    
    def cancel_click_one_purpose(self):
        self.element.click(self.purposeItem)

    def one_purpose_is_selected(self):
        active = self.element.get_attribute(self.purposeItem, 'class')
        self.element.should_contains(active, 'active')
    
    def one_purpose_is_not_selected(self):
        active = self.element.get_attribute(self.purposeItem, 'class')
        self.element.should_be_equal(active, 'list-item')

    def done_purposeModal(self):
        self.element.click(self.purposeModalDone)

    # def explain_is_email_registered(self):
    #     self.element.is_element_exist(self.explain_is_exit)

    # def explain_is_please_enter_email(self):
    #     self.element.is_element_exist(self.explain_is_exit)

    # def explain_is_please_enter_password(self):
    #     self.element.is_element_exist(self.explain_is_exit)

    # def check_prompt_is_password_less_6_characters(self):
    #     self.element.is_element_exist(self.explain_is_exit)
