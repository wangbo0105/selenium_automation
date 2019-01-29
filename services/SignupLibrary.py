from robot.api.deco import keyword
from pages.signuppage import Signuppage
from services.CommonLibrary import CommonLibrary

class SignupLibrary(object):
    cl = CommonLibrary()

    def __init__(self):
        self.signup = Signuppage()

    @keyword
    def sign_up(self, email, username, password):
      self.signup.input_email(email)
      self.signup.input_username(username)
      self.signup.input_password(password)
      self.signup.submit()

    @keyword
    def signup_success(self):
      self.signup.signup_success()

        
