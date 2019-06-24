from pages.basepage import BasePage
from module.random_generator import RandomGenerator
import time


class SettingsPage(BasePage):
    setting = ('link_text', '设置', 0)  # 用户tab——设置
    user_tab = ('class', 'ant-dropdown-trigger', 0)  # 用户tab
    page_title = ('class', 'inner-page-title', 0)  # 设置title
    name = ('id', 'name', 0)  # 昵称输入栏
    username = ('id', 'username', 0)  # 用户名输入栏
    personal_description = ('id', 'description', 0)  # 自我介绍输入栏
    personal_website = ('id', 'homepage', 0)  # 个人网站输入栏
    save_btn = ('class', 'save-btn', 0)  # 保存按钮

    def __init__(self):
        super().__init__()
        self.random_name = RandomGenerator().random_comments(5)
        self.random_username = RandomGenerator().random_comments(10)
        self.random_description = RandomGenerator().random_comments(16)

    def go_settings_page(self):
        self.element.move_to_element(self.user_tab)
        self.element.click(self.setting)

    def input_name(self):
        self.element.double_click(self.name)
        self.element.backSpace(self.name)
        self.element.send_keys(self.name, self.random_name)

    def input_username(self):
        self.element.double_click(self.username)
        self.element.backSpace(self.username)
        self.element.send_keys(self.username, self.random_username)

    def input_description(self):
        self.element.double_click(self.personal_description)
        self.element.backSpace(self.personal_description)
        self.element.send_keys(self.personal_description, self.random_description)

    def click_save_btn(self):
        self.element.click(self.save_btn)
        time.sleep(2)

    def is_settings_page(self):
        self.window.is_text_in_url('settings')
        self.element.is_element_exist(self.page_title)

    def is_edit(self, value='value'):
        self.element.is_input_text(self.name, value, self.random_name)
        self.element.is_input_text(self.username, value, self.random_username)
        self.element.is_input_text(self.personal_description, value, self.random_description)
