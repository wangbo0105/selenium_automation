from robot.api.deco import keyword
from pages.basepage import BasePage
from pages.bookmark import BookMark
from services.PhotoLibrary import PhotoLibrary
from services.CommonLibrary import CommonLibrary


class BookMarkLibrary(object):
    def __init__(self):
        self.base = BasePage()
        self.cl = CommonLibrary()
        self.bm = BookMark()
        self.pp = PhotoLibrary()

    @keyword
    def photo_bookmark(self):
        self.cl.go_page('全景图')
        self.pp.go_photo_detail()
        self.bm.click_bookmark_btn()
        self.bm.click_bookmark_alert_close_btn()

    @keyword
    def check_bookmark(self):
        self.bm.check_bookmark_in_detail_page()
        self.cl.go_page('VR书签')
        self.bm.check_bookmark_in_personalpage()

    @keyword
    def clear_bookmark(self):
        self.bm.clear_bookmark_all()
