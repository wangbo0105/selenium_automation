from robot.api.deco import keyword
from pages.bookmark import BookMark
from services.PhotoLibrary import PhotoLibrary
from services.CommonLibrary import CommonLibrary
from services.PersonalLibrary import PersonalLibrary


class BookMarkLibrary(object):
    def __init__(self):
        self.common = CommonLibrary()
        self.bookmark = BookMark()
        self.photo = PhotoLibrary()
        self.personal = PersonalLibrary()

    @keyword
    def go_bookmark_tab(self):
        self.personal.go_personal_center()
        self.personal.switch_nav_tab('VR书签')

    @keyword
    def bookmark_in_detail_page(self):
        self.common.go_page('photo')
        self.photo.photo_click_item('photo_content')
        self.bookmark.click_bookmark_btn()
        self.bookmark.click_bookmark_alert_close_btn()
        self.bookmark.check_bookmark_in_detail_page()

    @keyword
    def bookmark_in_cover_page(self):
        self.common.go_page('video')
        self.bookmark.click_bookmark_icon()
        self.bookmark.check_bookmark_in_surface()

    @keyword
    def Check_the_bookmark_has_been_added(self):
        self.go_bookmark_tab()
        self.bookmark.check_bookmark_in_personalpage()

    @keyword
    def remove_bookmark_in_detail(self):
        self.common.go_page('photo')
        self.photo.photo_click_item('photo_content')
        self.bookmark.remove_bookmark_in_detail()

    @keyword
    def check_remove_bookmark_in_detail(self):
        self.bookmark.check_remove_bookmark_in_detail()

    @keyword
    def check_remove_bookmark_in_personal(self):
        self.go_bookmark_tab()
        self.bookmark.check_remove_bookmark_in_personal()

    @keyword
    def click_bookmark_helper_button(self):
        self.bookmark.click_bookmark_helper_btn()

    @keyword
    def check_bookmark_helper_alert(self):
        self.bookmark.check_bookmark_helper_alert()

    @keyword
    def screen_bookmark_type(self, name):
        self.bookmark.switch_screen_type(name)

    @keyword
    def check_current_screen_type(self, name):
        self.bookmark.check_screen_results(name)

    @keyword
    def clear_bookmark_data(self):
        self.bookmark.clear_bookmark_all()
