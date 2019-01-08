from robot.api.deco import keyword
from pages.homepage import Homepage
from services.CommonLibrary import CommonLibrary


class HomeLibrary(Homepage):
    cl = CommonLibrary()

    @keyword
    def is_home_page(self):
        self.is_url(self.cl.url)
        self.isElementExist(self.veer_mark_text)
