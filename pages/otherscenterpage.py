from pages.basepage import BasePage


class OthersCenterPage(BasePage):
    user_name = ('css', 'div.avatar-info > div > div.name > a', 0)
    user_name_of_profile = ('css', 'div.user-infobox > div.main > div.mid > a', 0)

    def __init__(self):
        super().__init__()
        self.name1 = None

    def get_username(self, ele):
        return self.element.get_text(ele)

    def click_username(self):
        self.name1 = self.get_username(self.user_name)
        self.element.click(self.user_name)

    def should_be_expect_other_center(self):
        self.element.should_be_equal(self.name1, self.get_username(self.user_name_of_profile))
