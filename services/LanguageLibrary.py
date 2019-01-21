from robot.api.deco import keyword
from pages.languagepage import Languagepage
from services.CommonLibrary import CommonLibrary


class LanguageLibrary(object):

    def __init__(self):
        self.lan = Languagepage()

    @keyword
    def switch_english(self):
        self.lan.click_language_box()
        self.lan.click_english()

    @keyword
    def is_english(self):
        self.lan.is_english()

    @keyword
    def switch_japanese(self):
        self.lan.click_language_box()
        self.lan.click_japanese()

    @keyword
    def is_japanese(self):
        self.lan.is_japanese()
