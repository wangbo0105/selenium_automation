from pages.basepage import BasePage


class Personalpage(object):
    personal_center = ('link_text', '个人中心', 0)  # 用户tab——个人中心
    user_tab = ('class', 'ant-dropdown-trigger', 0)  # 用户tab
    home_tab = ('class', 'tabs-tab', 0)  # 个人中心-主页tab

    def __init__(self):
        self.base = BasePage()

    def is_personal_page(self):
        self.base.window.is_text_in_url('home')
        self.base.element.is_element_exist(self.home_tab)
