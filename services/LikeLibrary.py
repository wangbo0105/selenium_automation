from robot.api.deco import keyword
from pages.like import Like
from services.PersonalLibrary import PersonalLibrary


class LikeLibrary(object):
    def __init__(self):
        self.like = Like()
        self.personal = PersonalLibrary()

    @keyword
    def go_liked_tab(self):
        self.personal.go_personal_center()
        self.personal.switch_nav_tab('喜欢')

    @keyword
    def add_content_like(self):
        self.like.click_like_button()

    @keyword
    def remove_content_liked(self):
        self.like.click_unlike_button()

    @keyword
    def check_content_is_liked(self, name):
        self.like.check_liked_in_detail_page()
        self.go_liked_tab()
        self.like.check_liked_type_exited(name)
        self.like.check_liked_content_exited(name)

    # @keyword
    # def check_liked_type_tab_exited(self, name):
    #     self.like.check_liked_type_exited(name)

    @keyword
    def check_liked_content_is_remove_in_detail(self):
        self.like.check_unlike_in_detail_page()

    @keyword
    def check_liked_content_is_removed_in_liked_tab(self, name):
        self.go_liked_tab()
        self.like.check_liked_content_removed(name)

    @keyword
    def click_liked_content_in_liked_tab(self, name):
        self.like.click_liked_tab_content(name)

    @keyword
    def clear_all_liked_content(self):
        self.like.clear_like_all()
