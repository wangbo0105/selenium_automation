from robot.api.deco import keyword
from pages.personalpage import Personalpage
from services.CommonLibrary import CommonLibrary


class PersonalLibrary(Personalpage):
    cl = CommonLibrary()

    @keyword
    def go_personal(self):
        self.cl.goto_page_by_hover(self.user_tab, self.personal_center)

    @keyword
    def is_personal_page(self):
        self.is_text_in_url('home')
        self.isElementExist2(self.home_tab)
