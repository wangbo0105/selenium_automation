from pages.basepage import BasePage


class PersonalPage(BasePage):
    personal_center = ('link_text', '个人中心', 0)  # 用户tab——个人中心
    user_tab = ('class', 'ant-dropdown-trigger', 0)  # 用户tab
    home_tab = ('class', 'tabs-tab', 0)  # 个人中心-主页tab

    def go_personal_page(self):
        self.element.move_to_element(self.user_tab)
        self.element.click(self.personal_center)

    def is_personal_page(self):
        self.window.is_text_in_url('home')
        self.element.is_element_exist(self.home_tab)
