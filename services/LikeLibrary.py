from robot.api.deco import keyword
from pages.like import Like
from services.PhotoLibrary import PhotoLibrary
from services.PersonalLibrary import PersonalLibrary


class LikeLibrary(Like):
    pp = PhotoLibrary()
    per = PersonalLibrary()
    photo_url = None

    @keyword
    def photo_content_like(self):
        self.pp.go_photo()
        self.pp.go_photo_detail()
        self.click_like_button()
        self.photo_url = self.get_current_url()

    @keyword
    def check_liked_in_detail_page(self):
        self.is_element_exist(self.liked_button)

    @keyword
    def go_like_page(self):
        self.per.go_personal()
        self.click_like_tab()

    @keyword
    def check_liked_in_like_page(self):
        self.should_be_equal(self.photo_url, self.get_content_href_1())
