from robot.api.deco import keyword
from pages.photopage import Photopage
from services.CommonLibrary import CommonLibrary


class PhotoLibrary(object):
    def __init__(self):
        self.cl = CommonLibrary()
        self.photopage = Photopage()

    @keyword
    def go_photo_detail(self):
        self.photopage.click_photo_content_1()

    @keyword
    def is_photo_page(self):
        self.photopage.is_photo_page()

    @keyword
    def is_photo_detail_page(self):
        self.photopage.is_photo_detail_page()
