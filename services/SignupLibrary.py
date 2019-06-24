from robot.api.deco import keyword
from pages.signuppage import SignupPage
from services.CommonLibrary import CommonLibrary
from pages.loginpage import LoginPage
import time


class SignupLibrary(object):
    cl = CommonLibrary()

    def __init__(self):
        self.signup = SignupPage()
        self.login = LoginPage()

    @keyword
    def select_signup(self):
        self.signup.clickSignupButton()

    def sign_up(self, email=None, username=None, password=None, fullname=None, ExpectedResult=True):
        self.signup.select_email()
        self.signup.input_email(email)
        self.signup.input_username(username)
        self.signup.input_password(password)
        # self.signup.input_nickname(nickname)
        self.signup.input_fullname(fullname)
        self.signup.submit()
        if ExpectedResult == 'False':
            self.close_signup_modal()

    @keyword
    def signup_success(self):
        self.signup.signup_success()

    # @keyword
    # def has_purpose_modal(self):
    #     self.signup.is_exist_purposeModal()

    # @keyword
    # def check_one_purpose(self):
    #     self.signup.click_one_purpose()

    # @keyword
    # def one_purpose_is_selected(self):
    #     self.signup.one_purpose_is_selected()

    # @keyword
    # def check_cancel_one_purpose(self):
    #     self.signup.cancel_click_one_purpose()
    #     self.signup.one_purpose_is_not_selected()

    # @keyword
    # def skip_purpose_and_sign_out(self):
    #     self.signup.skip_purposeModal()
    #     time.sleep(3)
    #     self.login.hover_user_tab()
    #     self.login.click_log_out()

    # @keyword
    # def close_purpose_modal_and_sign_out(self):
    #     self.signup.click_purposeModalCloseBtn()
    #     time.sleep(3)
    #     self.login.hover_user_tab()
    #     self.login.click_log_out()

    # @keyword
    # def select_done_and_sign_out(self):
    #     self.signup.done_purposeModal()
    #     time.sleep(3)
    #     self.login.hover_user_tab()
    #     self.login.click_log_out()

    @keyword
    def close_signup_modal(self):
        self.signup.click_signupModalClose()

    # 注释代码是暂时还未实现的check各种注册失败情况下的文案提示
    # @keyword
    # def check_prompt_is_email_has_already_registered(self):
    #     self.signup.explain_is_email_registered()

    # @keyword
    # def check_prompt_is_please_enter_email(self):
    #     self.signup.explain_is_please_enter_email()

    # @keyword
    # def check_prompt_is_email_is_invalid(self):
    #     self.signup.explain_is_please_enter_email()

    # @keyword
    # def check_prompt_is_please_enter_password(self):
    #     self.signup.explain_is_please_enter_password()

    # @keyword
    # def check_prompt_is_password_less_6_characters(self):
    #     self.signup.check_prompt_is_password_less_6_characters()
