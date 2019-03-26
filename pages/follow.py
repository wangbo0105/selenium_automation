from pages.basepage import BasePage


class Follow(BasePage):
    creater_name = ('class', 'user-name', 1)
    follow_btn = ('class', 'follow-btn', 0)
    followed_btn = ('class', 'followed-btn', 0)
    following_btn = ('class', 'following', 0)
    follower_btn = ('class', 'follower', 0)
    follower_name = ('xpath', '//div[@class="follower-item"]/div[@class="user-info"]/div/a', 0)
    followed_num_1 = ('css', 'div.following > div.number', 0)
    followed_num_2 = ('css', 'div.tabs-nav > div > a', 0)
    ant_btn_ghost = ('class', 'ant-btn-lg', 0)
    ant_btn_primary = ('class', 'ant-btn-lg', 1)
    container = ('class', 'content-container', 0)

    def __init__(self):
        super().__init__()
        self.c_name = None

    def go_following_page(self):
        self.element.click(self.following_btn)

    def check_following_page(self):
        self.window.is_text_in_url('following')
        self.element.is_element_exist(self.container)

    def go_follower_page(self):
        self.element.click(self.follower_btn)

    def check_follower_page(self):
        self.window.is_text_in_url('follower')
        self.element.is_element_exist(self.container)

    def go_follower_home_page(self):
        self.element.click(self.follower_name)

    def click_follow_btn(self):
        self.element.click(self.follow_btn)
        self.c_name = self.element.get_text(self.creater_name)

    def click_following_btn(self):
        self.element.click(self.following_btn)

    def check_follow_state_in_detail_page(self, type):
        if type:
            self.element.is_element_exist(self.followed_btn)
        else:
            self.element.is_element_exist(self.follow_btn)

    def check_follow_state_in_follow_page(self, type):
        if type:
            self.element.should_be_equal(self.element.get_text(self.creater_name), self.c_name)
            self.element.is_element_exist(self.followed_btn)
        else:
            self.element.is_element_not_exist(self.followed_btn)

    def check_followed_num_in_personal_center(self, num):
        _num = self.element.get_text(self.followed_num_1)
        self.element.should_be_equal(_num, num)

    def check_followed_num_in_following_page(self, num):
        _num = self.element.get_text(self.followed_num_2)
        self.element.should_contains(_num, num)

    def click_followed_button(self):
        self.c_name = self.element.get_text(self.creater_name)
        self.element.click(self.followed_btn)

    def select_follow_type(self, type):
        if type:
            self.element.click(self.ant_btn_primary)
        else:
            self.element.click(self.ant_btn_ghost)

    def clear_follow_all(self):
        while self.element.ElementExist(self.followed_btn):
            self.element.click(self.followed_btn)
            self.element.click(self.ant_btn_primary)
            self.browser.refresh()
