from pages.basepage import BasePage


class Languagepage(BasePage):
    langs = ('class', 'langs')  # 语言切换栏
    english_tab = ('class', 'lang')  # English
    japanese_tab = ('class', 'lang', 1)  # Japanese
    veer_mark_text = ('class', 'app-des')  # 环 球 V R 内 容 社 区
    english_mark_text = 'Global VR Content Community'
    japanese_mark_text = 'グローバルVRコンテンツコミュニティ'

    def click_language_box(self):
        self.click(self.findElement(self.langs))

    def click_english(self):
        self.click(self.findElement(self.english_tab))

    def click_japanese(self):
        self.click(self.findElements(self.japanese_tab))
