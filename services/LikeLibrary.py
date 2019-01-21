from robot.api.deco import keyword
from pages.like import Like
from services.PhotoLibrary import PhotoLibrary
from services.CommonLibrary import CommonLibrary


class LikeLibrary(object):
    def __init__(self):
        self.like = Like()
        self.cl = CommonLibrary()
        self.pp = PhotoLibrary()

    @keyword
    def photo_content_like(self):
        self.cl.go_page('全景图')
        self.pp.go_photo_detail()
        self.like.click_like_button()

    @keyword
    def check_liked(self):
        self.like.check_liked_in_detail_page()
        self.cl.go_page('喜欢')
        self.like.check_liked_in_like_page()
