from robot.api.deco import keyword
from pages.photopage import PhotoPage
from services.CommonLibrary import CommonLibrary


class PhotoLibrary(object):
    def __init__(self):
        self.cl = CommonLibrary()
        self.photopage = PhotoPage()

    @keyword
    def click_item(self, name):
        self.photopage.click_item(name)

    @keyword
    def is_selected_banner_tab(self, name):
        self.photopage.is_selected_tab(name)

    @keyword
    def is_photo_page(self):
        self.photopage.match_video_url()
        self.photopage.is_photo_page()

    @keyword
    def is_photo_detail_page(self):
        self.photopage.match_video_url()
        self.photopage.is_photo_detail_page()

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


