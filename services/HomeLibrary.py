from robot.api.deco import keyword
from pages.homepage import HomePage


class HomeLibrary(object):
    def __init__(self):
        self.homepage = HomePage()

    @keyword
    def should_be_home_page(self):
        self.homepage.home_page()

    @keyword
    def go_recommended_page(self):
        self.homepage.click_recommended_view_all()

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
