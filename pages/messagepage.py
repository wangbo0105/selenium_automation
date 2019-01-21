from pages.basepage import BasePage


class Messagepage(object):
    message_box = ('class', 'message-box-header', 0)  # 导航栏-消息盒子
    page_bar_title = ('class', 'inner-page-title', 0)  # 消息盒子页面-消息标识
    bar_title = '消息'

    def __init__(self):
        self.base = BasePage()

    def is_message_page(self):
        self.base.window.is_text_in_url('messages')
        self.base.element.is_text_in_element(self.page_bar_title, self.bar_title)

