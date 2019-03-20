from pages.basepage import BasePage


class Language(BasePage):
    langs = ('class', 'langs', 0)
    veer_mark_text = ('class', 'app-des', 0)

    @staticmethod
    def language_type_dict(name):
        item_name = {
            'English': ('xpath', "//div[contains(text(),'English')]", 0),
            'Chinese': ('xpath', "//div[contains(text(),'中文简体')]", 0),
            'Japanese': ('xpath', "//div[contains(text(),'日本語')]", 0),
            }
        return item_name[name]

    def switch_language(self, name):
        self.element.move_to_element(self.langs)
        self.element.click(self.langs)
        self.element.click(self.language_type_dict(name))

    @staticmethod
    def language_item_dict(name):
        item_name = {'English': 'Global VR Content Community',
                     'Chinese': '环 球 V R 内 容 社 区',
                     'Japanese': 'グローバルVRコンテンツコミュニティ',
                     }
        return item_name[name]

    def check_current_language(self, name):
        self.element.is_text_in_element(self.veer_mark_text, self.language_item_dict(name))
        self.element.is_element_exist(self.language_type_dict(name))
