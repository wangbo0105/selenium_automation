from pages.basepage import BasePage


class Follow(object):
    creater_name = ('class', 'user-name', 1)  # 作者昵称
    follow_btn = ('class', 'follow-btn', 0)  # 关注 button
    followed_btn = ('class', 'followed-btn', 0)  # 已关注 button
    following_btn = ('class', 'following', 0)  # 个人中心-关注button

    def __init__(self):
        self.base = BasePage()
        self.c_name = None

    def click_follow_btn(self):
        self.base.element.click(self.follow_btn)
        self.c_name = self.base.element.get_text(self.creater_name)

    def click_following_btn(self):
        self.base.element.click(self.following_btn)

    def check_follow_in_detail_page(self):
        self.base.element.is_element_exist(self.followed_btn)

    def check_follow_in_follow_page(self):
        current_c_name = self.base.element.get_text(self.creater_name)
        self.base.element.should_be_equal(current_c_name, self.c_name)
