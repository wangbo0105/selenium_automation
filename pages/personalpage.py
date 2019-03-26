from pages.basepage import BasePage
import time


class PersonalPage(BasePage):
    personal_center = ('link_text', '个人中心', 0)  # 用户tab——个人中心
    user_tab = ('class', 'ant-dropdown-trigger', 0)  # 用户tab
    home_tab = ('class', 'tabs-tab', 0)  # 个人中心-主页tab

    @staticmethod
    def tabs_nav_dict():
        item_name = {'主页': ('class', ' tabs-tab', 0),
                     '作品': ('class', ' tabs-tab', 1),
                     '合辑': ('class', ' tabs-tab', 2),
                     'VR书签': ('class', ' tabs-tab', 3),
                     '喜欢': ('class', ' tabs-tab', 4)}
        return item_name

    def get_tabs_nav_dict(self, name):
        item = self.tabs_nav_dict()
        return item[name]

    def switch_nav_tab(self, name):
        self.element.click(self.get_tabs_nav_dict(name))
        time.sleep(1)

    def check_tabs_is_selected(self, name):
        active = self.element.get_attribute(self.get_tabs_nav_dict(name), 'aria-selected')
        self.element.should_be_equal(active, 'true')

    def go_personal_page(self):
        self.element.move_to_element(self.user_tab)
        self.element.click(self.personal_center)

    def is_personal_page(self):
        self.window.is_text_in_url('home')
        self.element.is_element_exist(self.home_tab)
