from robot.api.deco import keyword
from pages.messagepage import Messagepage
from services.LoginLibrary import LoginLibrary


class MessageLibrary(Messagepage, LoginLibrary):
    @keyword
    def go_message(self):
        self.go_message_page()
