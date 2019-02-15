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
    def switch_window(self):
        self.base.window.switch_handle()

    @keyword
    def go_page(self, name):
        self.navigator.go_page(name)

    @keyword
    def url_should_be_matching(self, _regular):
        self.navigator.match_url(_regular)

    @keyword
    def should_be_expected_page(self, _page):
        self.navigator.check_current_page(_page)
