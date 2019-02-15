from robot.api.deco import keyword
from pages.follow import Follow
from pages.basepage import BasePage
from services.PhotoLibrary import PhotoLibrary
from services.CommonLibrary import CommonLibrary
from services.PersonalLibrary import PersonalLibrary


class FollowLibrary(object):

    def __init__(self):
        self.common = CommonLibrary()
        self.follow = Follow()
        self.photo = PhotoLibrary()
        self.base = BasePage()
        self.personal = PersonalLibrary()

    @keyword
    def go_followed_page(self):
        self.follow.go_following_page()

    @keyword
    def follow_creater(self):
        self.common.go_page('photo')
        self.photo.photo_click_item('photo_content')
        self.follow.click_follow_btn()

    @keyword
    def Check_the_creator_is_focused_on_success(self):
        self.follow.check_follow_in_detail_page()
        self.follow.go_following_page()
        self.follow.check_follow_in_follow_page()

    @keyword
    def clear_following(self):
        self.follow.clear_follow_all()
