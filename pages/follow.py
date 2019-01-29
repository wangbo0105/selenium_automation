from pages.basepage import BasePage
from pages.personalpage import PersonalPage


class Follow(BasePage):
    creater_name = ('class', 'user-name', 1)  # 作者昵称
    follow_btn = ('class', 'follow-btn', 0)  # 关注 button
    followed_btn = ('class', 'followed-btn', 0)  # 已关注 button
    following_btn = ('class', 'following', 0)  # 个人中心-关注button

    def __init__(self):
        super().__init__()
        self.personal = PersonalPage()
        self.c_name = None

    def go_following_page(self):
        self.personal.go_personal_page()
        self.element.click(self.following_btn)

    def click_follow_btn(self):
        self.element.click(self.follow_btn)
        self.c_name = self.element.get_text(self.creater_name)

    def click_following_btn(self):
        self.element.click(self.following_btn)

    def check_follow_in_detail_page(self):
        self.element.is_element_exist(self.followed_btn)

    def check_follow_in_follow_page(self):
        current_c_name = self.element.get_text(self.creater_name)
        self.element.should_be_equal(current_c_name, self.c_name)
