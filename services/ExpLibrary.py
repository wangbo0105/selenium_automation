from robot.api.deco import keyword
from pages.exppage import Exppage


class ExpLibrary(Exppage):
    @keyword
    def go_exp(self):
        self.go_exp_page()

    @keyword
    def go_exp_detail(self):
        self.go_exp_detail_page()
