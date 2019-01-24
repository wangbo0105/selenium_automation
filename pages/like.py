from pages.basepage import BasePage


class Like(BasePage):
    like_button = ('class', 'like-button', 0)  # like-button
    liked_button = ('class', 'liked', 0)  # liked
    like_tab = ('class', ' tabs-tab', 4)  # 个人中心-喜欢tab
    content_href_1 = ('class', 'title', 1)  # 喜欢tab-第一个作品
    play_overlay = ('class', 'play-overlay', 0)  # 喜欢列表内容

    def __init__(self):
        super().__init__()
        self.photo_url = None

    def click_like_button(self):
        self.element.click(self.like_button)
        self.photo_url = self.window.get_current_url()

    def check_liked_in_detail_page(self):
        self.element.is_element_exist(self.liked_button)

    def click_like_tab(self):
        self.element.click(self.like_tab)

    def check_liked_in_like_page(self):
        href = self.element.get_attribute_href(self.content_href_1)
        self.element.should_be_equal(self.photo_url, href)

    def clear_like_all(self):
        while self.element.ElementExist(self.play_overlay):
            self.element.click(self.play_overlay)
            self.element.click(self.liked_button)
            self.browser.back()
        self.element.is_element_not_exist(self.play_overlay)
