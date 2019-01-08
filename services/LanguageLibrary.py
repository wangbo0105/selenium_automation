from robot.api.deco import keyword
from pages.languagepage import Languagepage
from services.CommonLibrary import CommonLibrary


class LanguageLibrary(Languagepage):
    cl = CommonLibrary()

    @keyword
    def switch_english(self):
        self.cl.goto_page_by_hover(self.langs, self.english_tab)

    @keyword
    def is_english(self):
        self.is_text_in_element(self.veer_mark_text, 'Global VR Content Community')

    @keyword
    def switch_japanese(self):
        self.cl.goto_page_by_hover(self.langs, self.japanese_tab)

    @keyword
    def is_japanese(self):
        self.is_text_in_element(self.veer_mark_text, 'グローバルVRコンテンツコミュニティ')


