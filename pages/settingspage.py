from pages.basepage import BasePage


class Settingspage(object):
    setting = ('link_text', '设置', 0)  # 用户tab——设置
    user_tab = ('class', 'ant-dropdown-trigger', 0)  # 用户tab
    page_title = ('class', 'inner-page-title', 0)  # 设置title
    name = ('id', 'name', 0)  # 昵称输入栏
    username = ('id', 'username', 0)  # 用户名输入栏
    personal_description = ('id', 'description', 0)  # 自我介绍输入栏
    personal_website = ('id', 'homepage', 0)  # 个人网站输入栏
    save_btn = ('class', 'save-btn', 0)  # 保存按钮

    def __init__(self):
        self.base = BasePage()

    def input_name(self, _name):
        self.base.element.double_click(self.name)
        self.base.element.backSpace(self.name)
        self.base.element.send_keys(self.name, _name)

    def input_username(self, _username):
        self.base.element.double_click(self.username)
        self.base.element.backSpace(self.username)
        self.base.element.send_keys(self.username, _username)

    def input_description(self, _des):
        self.base.element.double_click(self.personal_description)
        self.base.element.backSpace(self.personal_description)
        self.base.element.send_keys(self.personal_description, _des)

    def click_save_btn(self):
        self.base.element.click(self.save_btn)

    def is_settings_page(self):
        self.base.window.is_text_in_url('settings')
        self.base.element.is_element_exist(self.page_title)

    def is_edit(self, _name, _username, _des, value='value'):
        self.base.element.is_input_text(self.name, value, _name)
        self.base.element.is_input_text(self.username, value, _username)
        self.base.element.is_input_text(self.personal_description, value,  _des)
