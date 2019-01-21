from robot.api.deco import keyword
from pages.personalpage import Personalpage


class PersonalLibrary(object):

    def __init__(self):
        self.personal = Personalpage()

    @keyword
    def is_personal_page(self):
        self.personal.is_personal_page()
