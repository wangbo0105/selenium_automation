from robot.api.deco import keyword
from pages.exppage import Exppage


class ExpLibrary(object):
    def __init__(self):
        self.exp = Exppage()

    @keyword
    def click_item(self, name):
        self.exp.click_item(name)

    @keyword
    def is_exp_page(self):
        self.exp.is_exp_page()

    @keyword
    def is_exp_detail_page(self):
        self.exp.is_exp_detail_page()

    @keyword
    def is_banner_tab(self, name):
        self.exp.is_select_banner_tab(name)

    @keyword
    def is_Seth_home_page(self):
        self.exp.is_Seth_home_page()
