from robot.api.deco import keyword
from pages.photopage import Photopage
from services.CommonLibrary import CommonLibrary


class PhotoLibrary(Photopage):
    cl = CommonLibrary()

    @keyword
    def go_photo(self):
        self.cl.goto_page_by_click(self.photo_tab)

    @keyword
    def go_photo_detail(self):
        self.cl.goto_page_by_click(self.photo_box_1)

    @keyword
    def is_photo_page(self):
        self.is_text_in_url('photo')
        self.is_text_in_element(self.slogan, 'VeeR 360 全景图')

    @keyword
    def is_photo_detail_page(self):
        self.is_text_in_url('photos/')
        self.is_element_exist(self.photo_player)
