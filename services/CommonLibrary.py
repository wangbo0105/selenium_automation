from robot.api.deco import keyword
from pages.basepage import BasePage
from pages.navigator import Navigator


class CommonLibrary(object):
    def __init__(self):
        self.base = BasePage()
        self.navigator = Navigator()

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
        self.navigator.go_page(name)
