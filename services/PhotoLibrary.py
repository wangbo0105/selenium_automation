from robot.api.deco import keyword
from pages.photopage import PhotoPage
from services.CommonLibrary import CommonLibrary


class PhotoLibrary(object):
    def __init__(self):
        self.photopage = PhotoPage()
        self.common = CommonLibrary()

    @keyword
    def photo_click_item(self, name):
        self.photopage.click_item(name)

    @keyword
    def the_banner_tab_should_be_selected(self, name):
        self.photopage.is_selected_tab(name)

    @keyword
    def should_be_photo_detail_page(self):
        self.common.url_should_be_matching('photo')
        self.photopage.is_photo_detail_page()

    @keyword
    def turn_page(self):
        self.photopage.click_turn_page_btn()

    @keyword
    def the_pages_should_turned(self):
        self.photopage.is_turned_page()

    @keyword
    def click_more_photo_content(self):
        self.photopage.get_photo_content_title()
        self.photopage.click_more_photo()

    @keyword
    def should_be_more_photo_content_page(self):
        self.common.url_should_be_matching('photo')
        self.photopage.is_more_photo_page()
