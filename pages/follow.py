from pages.basepage import BasePage


class Follow(BasePage):
    creater_name = ('class', 'user-name', 1)  # 作者昵称
    follow_btn = ('class', 'follow-btn', 0)  # 关注 button
    followed_btn = ('class', 'followed-btn', 0)  # 已关注 button
    following_btn = ('class', 'following', 0)  # 个人中心-关注button

    def click_follow_btn(self):
        self.click(self.findElements(self.follow_btn))

    def click_following_btn(self):
        self.click(self.findElements(self.following_btn))
