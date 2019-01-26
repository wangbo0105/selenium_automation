from robot.api.deco import keyword
from pages.language import Language
from services.CommonLibrary import CommonLibrary


class LanguageLibrary(object):

    def __init__(self):
        self.language = Language()

    @keyword
    def switch_english(self):
        self.language.click_language_box()
        self.language.click_english()

    @keyword
    def check_english(self):
        self.language.is_english()

    @keyword
    def switch_japanese(self):
        self.language.click_language_box()
        self.language.click_japanese()

    @keyword
    def check_japanese(self):
        self.language.is_japanese()
