from pages.basepage import BasePage


class Settingspage(BasePage):
    setting = ('link_text', '设置', 0)  # 用户tab——设置
    user_tab = ('class', 'ant-dropdown-trigger', 0)  # 用户tab
    page_title = ('class', 'inner-page-title', 0)  # 设置title
    name = ('id', 'name', 0)  # 昵称输入栏
    username = ('id', 'username', 0)  # 用户名输入栏
    personal_description = ('id', 'description', 0)  # 自我介绍输入栏
    personal_website = ('id', 'homepage', 0)  # 个人网站输入栏
    save_btn = ('class', 'save-btn', 0)  # 保存按钮

    def input_name(self, _name):
        name_tab = self.findElements(self.name)
        self.double_click(name_tab)
        self.backSpace(name_tab)
        self.send_keys(name_tab, _name)

    def input_username(self, _username):
        username_tab = self.findElements(self.username)
        self.double_click(username_tab)
        self.backSpace(username_tab)
        self.send_keys(username_tab, _username)

    def input_description(self, _des):
        p_des = self.findElements(self.personal_description)
        self.double_click(p_des)
        self.backSpace(p_des)
        self.send_keys(p_des, _des)

    # def input_website(self, _website):
    #     p_web = self.findElement(self.personal_website)
    #     self.click(p_web)
    #     self.clear(p_web)
    #     self.send_keys(p_web, _website)

    def click_save_btn(self):
        self.click(self.findElements(self.save_btn))
