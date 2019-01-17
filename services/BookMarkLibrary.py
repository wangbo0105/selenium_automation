from robot.api.deco import keyword
from pages.bookmark import BookMark
from services.PhotoLibrary import PhotoLibrary
from services.PersonalLibrary import PersonalLibrary


class BookMarkLibrary(BookMark):
    pp = PhotoLibrary()
    per = PersonalLibrary()
    photo_url = None

    @keyword
    def go_bookmark_tab(self):
        self.per.go_personal()
        self.click_VR_tab()

    @keyword
    def photo_bookmark(self):
        self.pp.go_photo()
        self.pp.go_photo_detail()
        self.click_bookmark_btn()
        self.photo_url = self.get_current_url()

    @keyword
    def close_bookmark_alert(self):
        self.click_bookmark_alert_close_btn()

    @keyword
    def check_bookmark_in_detail_page(self):
        self.is_text_in_element(self.bookmark_btn, '已添加书签')

    @keyword
    def check_bookmark_in_personal_page(self):
        self.should_be_equal(self.photo_url, self.get_content_href_1())

    @keyword
    def clear_bookmark(self):
        self.clear_bookmark_all()

