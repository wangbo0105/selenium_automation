from robot.api.deco import keyword
from pages.messagepage import MessagePage


class MessageLibrary(object):

    def __init__(self):
        self.msg = MessagePage()

    @keyword
    def should_be_message_page(self):
        self.msg.is_message_page()

    @keyword
    def hover_and_click_seeallmessage(self):
        self.msg.hover_message_headerbar()
        self.msg.click_see_all_message()
