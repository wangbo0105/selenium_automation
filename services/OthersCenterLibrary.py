from robot.api.deco import keyword
from pages.otherscenterpage import OthersCenterPage


class OthersCenterLibrary(object):

    def __init__(self):
        self.ocl = OthersCenterPage()

    @keyword
    def should_be_otherscenter_page(self):
        self.ocl.is_othercenterpage()

    @keyword
    def click_username_from_list(self):
        self.ocl.click_username()
        self.ocl.get_username_from_profilepage()

    @keyword
    def click_content(self):
        self.ocl.click_content()
