from robot.api.deco import keyword
from pages.personalpage import Personalpage
from services.LoginLibrary import LoginLibrary


class PersonalLibrary(Personalpage, LoginLibrary):
    @keyword
    def go_personal(self):
        self.hover_user_tab()
        self.go_personal_center()
