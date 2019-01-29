from pages.basepage import BasePage


class SettingsPage(BasePage):
    setting = ('link_text', '设置', 0)  # 用户tab——设置
    user_tab = ('class', 'ant-dropdown-trigger', 0)  # 用户tab
    page_title = ('class', 'inner-page-title', 0)  # 设置title
    name = ('id', 'name', 0)  # 昵称输入栏
    username = ('id', 'username', 0)  # 用户名输入栏
    personal_description = ('id', 'description', 0)  # 自我介绍输入栏
    personal_website = ('id', 'homepage', 0)  # 个人网站输入栏
    save_btn = ('class', 'save-btn', 0)  # 保存按钮

    def go_settings_page(self):
        self.element.move_to_element(self.user_tab)
        self.element.click(self.setting)

    def input_name(self, _name):
        self.element.double_click(self.name)
        self.element.backSpace(self.name)
        self.element.send_keys(self.name, _name)

    def input_username(self, _username):
        self.element.double_click(self.username)
        self.element.backSpace(self.username)
        self.element.send_keys(self.username, _username)

    def input_description(self, _des):
        self.element.double_click(self.personal_description)
        self.element.backSpace(self.personal_description)
        self.element.send_keys(self.personal_description, _des)

    def click_save_btn(self):
        self.element.click(self.save_btn)

    def is_settings_page(self):
        self.window.is_text_in_url('settings')
        self.element.is_element_exist(self.page_title)

    def is_edit(self, _name, _username, _des, value='value'):
        self.element.is_input_text(self.name, value, _name)
        self.element.is_input_text(self.username, value, _username)
        self.element.is_input_text(self.personal_description, value,  _des)
