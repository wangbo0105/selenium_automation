from robot.api.deco import keyword
from pages.exppage import Exppage


class ExpLibrary(object):
    def __init__(self):
        self.exp = Exppage()

    @keyword
    def go_exp_detail(self):
        self.exp.click_learn_more_btn()

    @keyword
    def is_exp_page(self):
        self.exp.is_exp_page()

    @keyword
    def is_exp_detail_page(self):
        self.exp.is_exp_detail_page()
