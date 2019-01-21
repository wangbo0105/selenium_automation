from pages.basepage import BasePage


class Languagepage(object):
    langs = ('class', 'langs', 0)  # 语言切换栏
    english_tab = ('class', 'lang', 0)  # English
    japanese_tab = ('class', 'lang', 1)  # Japanese
    veer_mark_text = ('class', 'app-des', 0)  # 环 球 V R 内 容 社 区
    english_mark_text = 'Global VR Content Community'
    japanese_mark_text = 'グローバルVRコンテンツコミュニティ'

    def __init__(self):
        self.base = BasePage()

    def click_language_box(self):
        self.base.element.click(self.langs)

    def click_english(self):
        self.base.element.click(self.english_tab)

    def click_japanese(self):
        self.base.element.click(self.japanese_tab)

    def is_english(self):
        self.base.element.is_text_in_element(self.veer_mark_text, self.english_mark_text)

    def is_japanese(self):
        self.base.element.is_text_in_element(self.veer_mark_text, self.japanese_mark_text)
