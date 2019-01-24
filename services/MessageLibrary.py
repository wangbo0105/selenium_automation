from robot.api.deco import keyword
from pages.messagepage import MessagePage
from services.CommonLibrary import CommonLibrary


class MessageLibrary(object):
    cl = CommonLibrary()

    def __init__(self):
        self.msg = MessagePage()

    @keyword
    def is_message_page(self):
        self.msg.is_message_page()
