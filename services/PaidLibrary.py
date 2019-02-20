from robot.api.deco import keyword
from pages.paidpage import PaidPage
from services.CommonLibrary import CommonLibrary


class PaidLibrary(object):
    def __init__(self):
        self.paid = PaidPage()
        self.common = CommonLibrary()

    @keyword
    def should_be_paid_page(self):
        self.common.url_should_be_matching('paid')
        self.paid.is_paid_page()

    @keyword
    def should_be_paid_content_page(self):
        self.common.url_should_be_matching('contents')
        self.paid.is_paid_content_page()
