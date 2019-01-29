from robot.api.deco import keyword
from pages.like import Like
from services.PhotoLibrary import PhotoLibrary
from services.CommonLibrary import CommonLibrary
from services.PersonalLibrary import PersonalLibrary


class LikeLibrary(object):
    def __init__(self):
        self.like = Like()
        self.common = CommonLibrary()
        self.photo = PhotoLibrary()
        self.personal = PersonalLibrary()

    @keyword
    def go_liked_tab(self):
        self.like.go_liked_tab()

    @keyword
    def add_photos_like(self):
        self.common.go_page('photo')
        self.photo.photo_click_item('photo_content')
        self.like.click_like_button()

    @keyword
    def check_the_photo_is_liked(self):
        self.like.check_liked_in_detail_page()
        self.like.go_liked_tab()
        self.like.check_liked_in_like_page()
