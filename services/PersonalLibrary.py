from robot.api.deco import keyword
from pages.personalpage import PersonalPage


class PersonalLibrary(object):

    def __init__(self):
        self.personal = PersonalPage()

    def go_personal_center(self):
        self.personal.go_personal_page()

    @keyword
    def should_be_personal_page(self):
        self.personal.is_personal_page()

    @keyword
    def switch_nav_tab(self, name):
        self.personal.switch_nav_tab(name)

    @keyword
    def check_tabs_is_selected(self, name):
        self.personal.check_tabs_is_selected(name)
