from robot.api.deco import keyword
from pages.languagepage import Languagepage
from services.CommonLibrary import CommonLibrary


class LanguageLibrary(Languagepage):

    @keyword
    def switch_english(self):
        self.click_language_box()
        self.click_english()

    @keyword
    def is_english(self):
        self.is_text_in_element(self.veer_mark_text, self.english_mark_text)

    @keyword
    def switch_japanese(self):
        self.click_language_box()
        self.click_japanese()

    @keyword
    def is_japanese(self):
        self.is_text_in_element(self.veer_mark_text, self.japanese_mark_text)
