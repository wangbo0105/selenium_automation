from robot.api.deco import keyword
from pages.photopage import PhotoPage
from services.CommonLibrary import CommonLibrary


class PhotoLibrary(object):
    def __init__(self):
        self.cl = CommonLibrary()
        self.photopage = PhotoPage()

    @keyword
    def go_photo_detail(self):
        self.photopage.get_photo_content_title()
        self.photopage.click_photo_content_1()

    @keyword
    def is_photo_page(self):
        self.photopage.is_photo_page()

    @keyword
    def is_photo_detail_page(self):
        self.photopage.is_photo_detail_page()

    @keyword
    def click_featured_tab(self):
        self.photopage.click_featured_tab()

    @keyword
    def is_featured_tab(self):
        self.photopage.is_featured_tab()

    @keyword
    def click_popular_tab(self):
        self.photopage.click_popular_tab()

    @keyword
    def is_popular_tab(self):
        self.photopage.is_popular_tab()

    @keyword
    def click_recent_tab(self):
        self.photopage.click_recent_tab()

    @keyword
    def is_recent_tab(self):
        self.photopage.is_recent_tab()

    @keyword
    def turn_page(self):
        self.photopage.click_turn_page_btn()

    @keyword
    def is_turned_page(self):
        self.photopage.is_turned_page()

    @keyword
    def click_more_photo_content(self):
        self.photopage.get_photo_content_title()
        self.photopage.click_more_photo()

    @keyword
    def is_more_photo_content_page(self):
        self.photopage.is_more_photo_page()


