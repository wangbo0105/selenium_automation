from pages.basepage import BasePage


class MessagePage(BasePage):
    message_box = ('class', 'message-box-header', 0)  # 导航栏-消息盒子
    page_bar_title = ('class', 'inner-page-title', 0)  # 消息盒子页面-消息标识
    bar_title = '消息'
    see_all_message = ('class', 'all-msg',0) # 查看全部按钮

    def is_message_page(self):
        self.window.is_text_in_url('messages')
        self.element.is_text_in_element(self.page_bar_title, self.bar_title)

    def hover_message_headerbar(self):
        self.element.move_to_element(self.message_box)

    def click_see_all_message(self):
        self.element.click(self.see_all_message)

