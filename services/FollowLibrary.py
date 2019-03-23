from robot.api.deco import keyword
from pages.follow import Follow
from services.PersonalLibrary import PersonalLibrary


class FollowLibrary(object):

    def __init__(self):
        self.follow = Follow()
        self.personal = PersonalLibrary()

    @keyword
    def go_following_page(self):
        self.personal.go_personal_center()
        self.follow.go_following_page()

    @keyword
    def check_current_page_is_following_page(self):
        self.follow.check_following_page()

    @keyword
    def go_follower_page(self):
        self.personal.go_personal_center()
        self.follow.go_follower_page()

    @keyword
    def go_follower_homepage(self):
        self.follow.go_follower_home_page()

    @keyword
    def check_current_page_is_follower_page(self):
        self.follow.check_follower_page()

    @keyword
    def click_follow_btn(self):
        self.follow.click_follow_btn()

    @keyword
    def click_followed_btn(self):
        self.follow.click_followed_button()

    @keyword
    def check_follow_state_in_detail_page(self, type):
        self.follow.check_follow_state_in_detail_page(type)

    @keyword
    def check_follow_state_in_following_page(self, type):
        self.follow.check_follow_state_in_follow_page(type)

    @keyword
    def check_followed_num(self, num):
        self.personal.go_personal_center()
        self.follow.check_followed_num_in_personal_center(num)
        self.follow.go_following_page()
        self.follow.check_followed_num_in_following_page(num)

    @keyword
    def choose_follow_operation(self, type):
        self.follow.select_follow_type(type)

    @keyword
    def follow_creater_in_creater_home_page(self):
        self.go_follower_page()
        self.follow.go_follower_home_page()
        self.click_follow_btn()

    @keyword
    def clear_following(self):
        self.follow.clear_follow_all()
