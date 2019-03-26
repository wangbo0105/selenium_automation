from robot.api.deco import keyword
from pages.homepage import HomePage


class HomeLibrary(object):
    def __init__(self):
        self.homepage = HomePage()

    @keyword
    def click_feeds_item(self, name):
        self.homepage.click_feeds_item(name)

    @keyword
    def click_feeds_content_item(self, name):
        self.homepage.click_feeds_content_item(name)

    @keyword
    def should_be_recommended_page(self):
        self.homepage.recommended_page()

    @keyword
    def go_recommended_content_detail_page(self):
        self.homepage.get_recommended_content_href()
        self.homepage.click_recommended_content()

    @keyword
    def should_be_recommended_content_detail_page(self):
        self.homepage.recommended_content_detail_page()

    @keyword
    def click_more_recommended(self):
        self.homepage.click_recommended_show_more()

    @keyword
    def check_recommended_show_more_successful(self):
        self.homepage.recommended_show_more()

    @keyword
    def click_category_tab(self, name):
        self.homepage.click_category_tab(name)

    @keyword
    def check_category_page(self, name):
        self.homepage.check_category_page(name)

    @keyword
    def turning_list(self, _direction):
        self.homepage.turning_page(_direction)

    @keyword
    def check_turned_wrapper(self, item):
        self.homepage.is_turned_wrapper(item)
