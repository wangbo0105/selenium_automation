from pages.basepage import BasePage


class OthersCenterPage(BasePage):
    user_photo_of_list = ('class', 'el-overlay', 0)   # 第一个用户头像
    user_name = ('class', 'user-name', 0)   # 第一个用户昵称
    user_name_of_profile = ('class', 'user-name', 0)   # 用户主页的昵称
    username_of_contentdetail = ('class', 'user-name', 0)
    content_of_list = ('class', 'cover-stats', 0)


    def __init__(self):
        super().__init__()
        self.name1 = None
        self.name2 = None

    def click_username(self):
        self.name1 = self.element.get_text(self.user_name)
        self.element.click(self.user_name)

    def get_username_from_profilepage(self):
        self.name2 = self.element.get_text(self.user_name_of_profile)

    def is_othercenterpage(self):
        self.element.should_be_equal(self.name1, self.name2)

    def click_content(self):
        self.element.click(self.content_of_list)

