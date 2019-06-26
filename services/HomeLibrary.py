from robot.api.deco import keyword
from pages.homepage import HomePage
from pages.navigator import Navigator


class HomeLibrary(object):
    def __init__(self):
        self.homepage = HomePage()
        self.nav = Navigator()

    @keyword
    def go_recommend_page(self):
        self.homepage.click_recommended_item()

    @keyword
    def should_be_recommended_page(self):
        self.homepage.recommended_page()

    @keyword
    def go_recommended_content_detail_page(self):
        self.homepage.get_content_href()
        self.homepage.click_recommended_content()

    @keyword
    def go_channel_content_detail_page(self):
        self.homepage.get_content_href(False)
        self.homepage.click_channel_content()

    @keyword
    def should_be_content_detail_page(self):
        self.homepage.content_detail_page()

    @keyword
    def click_more_recommended(self):
        self.homepage.click_recommended_show_more()

    @keyword
    def check_recommended_show_more_successful(self):
        self.homepage.recommended_show_more()

    @keyword()
    def select_discover_item(self, name):
        self.nav.select_discover_item(name)

    @keyword()
    def select_channel_list(self, name):
        self.homepage.select_channel(name)

    @keyword()
    def check_current_channel(self, name):
        self.homepage.check_current_channel(name)

    @keyword()
    def turn_channel_page(self, direction):
        self.homepage.turning_page(direction)
        self.homepage.is_turned_wrapper(direction)
