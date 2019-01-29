from robot.api.deco import keyword
from pages.exppage import ExpPage


class ExpLibrary(object):
    def __init__(self):
        self.exp = ExpPage()

    @keyword
    def exp_click_item(self, name):
        self.exp.click_item(name)

    @keyword
    def should_be_experience_page(self):
        self.exp.match_exp_url()
        self.exp.is_exp_page()

    @keyword
    def should_be_experience_details_page(self):
        self.exp.match_exp_url()
        self.exp.is_exp_detail_page()

    @keyword
    def check_banner_tab_is_selected(self, name):
        self.exp.is_select_banner_tab(name)

    @keyword
    def should_be_Seth_personal_page(self):
        self.exp.is_Seth_home_page()
