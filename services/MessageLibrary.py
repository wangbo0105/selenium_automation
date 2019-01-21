from robot.api.deco import keyword
from pages.messagepage import Messagepage
from services.CommonLibrary import CommonLibrary


class MessageLibrary(object):
    cl = CommonLibrary()

    def __init__(self):
        self.msg = Messagepage()

    @keyword
    def is_message_page(self):
        self.msg.is_message_page()
