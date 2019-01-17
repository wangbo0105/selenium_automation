from pages.basepage import BasePage


class Like(BasePage):
    like_button = ('class', 'like-button', 0)  # like-button
    liked_button = ('class', 'liked', 0)  # liked
    like_tab = ('class', ' tabs-tab', 4)  # 个人中心-喜欢tab
    content_href_1 = ('class', 'title', 1)  # 喜欢tab-第一个作品
    play_overlay = ('class', 'play-overlay', 0)  # 喜欢列表内容

    def click_like_button(self):
        self.click(self.findElements(self.like_button))

    def click_like_tab(self):
        self.click(self.findElements(self.like_tab))

    def get_content_href_1(self):
        return self.get_attribute(self.findElements(self.content_href_1), 'href')

    def clear_like_all(self):
        while self.findElements(self.play_overlay):
            self.click(self.findElements(self.play_overlay))
            self.click(self.findElements(self.liked_button))
            self.back()
        self.is_element_not_exist(self.play_overlay)
