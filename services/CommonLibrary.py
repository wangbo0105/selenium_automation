import time

from robot.api.deco import keyword
from pages.basepage import BasePage
from pages.navigator import Navigator
from module.pagination import Pagination


class CommonLibrary(object):
    def __init__(self):
        self.base = BasePage()
        self.navigator = Navigator()
        self.pagination = Pagination()

    @keyword
    def load_veer(self):
        self.base.browser.open(self.base.url)
        # self.base.window.set_window_size(1400, 820)
        self.base.window.set_window_size(1600, 1000)
        time.sleep(1)

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

    @keyword
    def turn_current_tab_page(self, name):
        self.pagination.turn_page(name)

    @keyword
    def check_page_turned(self, name):
        self.pagination.check_page_active(name)
