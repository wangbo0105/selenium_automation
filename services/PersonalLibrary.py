from robot.api.deco import keyword
from pages.personalpage import PersonalPage


class PersonalLibrary(object):

    def __init__(self):
        self.personal = PersonalPage()

    @keyword
    def is_personal_page(self):
        self.personal.is_personal_page()
