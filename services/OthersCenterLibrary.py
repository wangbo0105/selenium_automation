from robot.api.deco import keyword
from pages.otherscenterpage import OthersCenterPage


class OthersCenterLibrary(object):

    def __init__(self):
        self.ocl = OthersCenterPage()

    @keyword
    def should_be_other_center_page(self):
        self.ocl.should_be_expect_other_center()

    @keyword
    def go_other_center(self):
        self.ocl.click_username()

