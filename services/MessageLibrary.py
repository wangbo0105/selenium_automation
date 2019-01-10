from robot.api.deco import keyword
from pages.messagepage import Messagepage
from services.CommonLibrary import CommonLibrary


class MessageLibrary(Messagepage):
    cl = CommonLibrary()

    @keyword
    def go_message(self):
        self.cl.goto_page_by_click(self.message_box)

    @keyword
    def is_message_page(self):
        self.is_text_in_url('messages')
        self.is_text_in_element(self.page_bar_title, self.bar_title)
