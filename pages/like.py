from pages.basepage import BasePage


class Like(object):
    like_button = ('class', 'like-button', 0)  # like-button
    liked_button = ('class', 'liked', 0)  # liked
    like_tab = ('class', ' tabs-tab', 4)  # 个人中心-喜欢tab
    content_href_1 = ('class', 'title', 1)  # 喜欢tab-第一个作品
    play_overlay = ('class', 'play-overlay', 0)  # 喜欢列表内容

    def __init__(self):
        self.base = BasePage()
        self.photo_url = None

    def click_like_button(self):
        self.base.element.click(self.like_button)
        self.photo_url = self.base.window.get_current_url()

    def check_liked_in_detail_page(self):
        self.base.element.is_element_exist(self.liked_button)

    def click_like_tab(self):
        self.base.element.click(self.like_tab)

    def check_liked_in_like_page(self):
        href = self.base.element.get_attribute_href(self.content_href_1)
        self.base.element.should_be_equal(self.photo_url, href)

    def clear_like_all(self):
        while self.base.element.ElementExist(self.play_overlay):
            self.base.element.click(self.play_overlay)
            self.base.element.click(self.liked_button)
            self.base.browser.back()
        self.base.element.is_element_not_exist(self.play_overlay)
