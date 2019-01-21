from robot.api.deco import keyword
from pages.follow import Follow
from pages.basepage import BasePage
from services.PhotoLibrary import PhotoLibrary
from services.CommonLibrary import CommonLibrary


class FollowLibrary(object):

    def __init__(self):
        self.cl = CommonLibrary()
        self.follow = Follow()
        self.pp = PhotoLibrary()
        self.base = BasePage()

    @keyword
    def follow_creater(self):
        self.cl.go_page('全景图')
        self.pp.go_photo_detail()
        self.follow.click_follow_btn()

    @keyword
    def check_follow(self):
        self.follow.check_follow_in_detail_page()
        self.cl.go_page('关注')
        self.follow.check_follow_in_follow_page()
