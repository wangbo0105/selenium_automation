from robot.api.deco import keyword
from pages.language import Language


class LanguageLibrary(object):

    def __init__(self):
        self.language = Language()

    @keyword
    def switch_language(self, name):
        self.language.switch_language(name)

    @keyword
    def check_current_language(self, name):
        self.language.check_current_language(name)
