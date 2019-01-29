from robot.api.deco import keyword
from pages.basepage import BasePage
from pages.bookmark import BookMark
from services.PhotoLibrary import PhotoLibrary
from services.CommonLibrary import CommonLibrary


class BookMarkLibrary(object):
    def __init__(self):
        self.base = BasePage()
        self.common = CommonLibrary()
        self.bookmark = BookMark()
        self.photo = PhotoLibrary()

    def go_bookmark_tab(self):
        self.bookmark.go_bookmark_tab()

    @keyword
    def bookmark_photos(self):
        self.common.go_page('photo')
        self.photo.photo_click_item('photo_content')
        self.bookmark.click_bookmark_btn()
        self.bookmark.click_bookmark_alert_close_btn()

    @keyword
    def Check_the_photo_bookmark_has_been_added(self):
        self.bookmark.check_bookmark_in_detail_page()
        self.bookmark.go_bookmark_tab()
        self.bookmark.check_bookmark_in_personalpage()

    @keyword
    def clear_bookmark_data(self):
        self.bookmark.clear_bookmark_all()
