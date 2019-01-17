from robot.api.deco import keyword
from pages.follow import Follow
from services.PhotoLibrary import PhotoLibrary
from services.PersonalLibrary import PersonalLibrary


class FollowLibrary(Follow):
    pp = PhotoLibrary()
    per = PersonalLibrary()
    c_name = None

    @keyword
    def follow_creater(self):
        self.pp.go_photo()
        self.pp.go_photo_detail()
        self.click_follow_btn()
        self.c_name = self.get_text(self.findElements(self.creater_name))

    @keyword
    def check_follow_in_detail_page(self):
        self.is_element_exist(self.followed_btn)

    @keyword
    def go_follow_page(self):
        self.per.go_personal()
        self.click_following_btn()

    @keyword
    def check_follow_in_follow_page(self):
        current_c_name = self.get_text(self.findElements(self.creater_name))
        self.should_be_equal(current_c_name, self.c_name)
