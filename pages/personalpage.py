from pages.basepage import BasePage


class Personalpage(BasePage):
    personal_center = ('link_text', '个人中心', 0)  # 用户tab——个人中心
    user_tab = ('class', 'ant-dropdown-trigger', 0)  # 用户tab
    home_tab = ('class', 'tabs-tab', 0)  # 个人中心-主页tab
