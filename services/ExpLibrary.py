from robot.api.deco import keyword
from pages.exppage import Exppage
from services.CommonLibrary import CommonLibrary


class ExpLibrary(Exppage):
    cl = CommonLibrary()

    @keyword
    def go_exp(self):
        self.cl.goto_page_by_click(self.exp_tab)

    @keyword
    def go_exp_detail(self):
        self.cl.goto_page_by_click(self.learn_more_1)

    @keyword
    def is_exp_page(self):
        self.is_text_in_url('experience')
        self.isElementExist(self.learn_more_1)

    @keyword
    def is_exp_detail_page(self):
        self.is_text_in_url('experiences/')
        self.isElementExist(self.load_layer)
