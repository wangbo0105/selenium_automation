from robot.api.deco import keyword
from pages.base import Base


class BrowserLibrary:

    @keyword
    def open_my_browser(self):
        self.base = Base()
        self.base.open('http://stg.veervr.tv')

    @keyword
    def close_my_browser(self):
        self.base.quit()
