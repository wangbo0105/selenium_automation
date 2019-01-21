from robot.api.deco import keyword
from pages.basepage import BasePage


class CommonLibrary:
    def __init__(self):
        self.base = BasePage()

    @keyword
    def load_veer(self):
        self.base.browser.open(self.base.url)

    @keyword
    def refresh_current_window(self):
        self.base.browser.refresh()

    @keyword
    def close_my_browser(self):
        self.base.browser.quit()

    @keyword
    def close_current_window(self):
        self.base.browser.close()

    @keyword
    def go_page(self, name):
        self.base.go_page(name)
