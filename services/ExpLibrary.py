from robot.api.deco import keyword
from pages.exppage import ExpPage
from services.CommonLibrary import CommonLibrary


class ExpLibrary(object):
    def __init__(self):
        self.exp = ExpPage()
        self.common = CommonLibrary()

    @keyword
    def exp_click_item(self, name):
        self.exp.click_item(name)

    @keyword
    def should_be_experience_details_page(self):
        self.common.url_should_be_matching('experience')
        self.exp.is_exp_detail_page()

    @keyword
    def check_banner_tab_is_selected(self, name):
        self.exp.is_select_banner_tab(name)

    @keyword
    def should_be_Seth_personal_page(self):
        self.exp.is_Seth_home_page()
