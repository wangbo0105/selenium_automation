from pages.basepage import BasePage


class PaidPage(BasePage):
    paid_feeds = ('class', 'paid-feeds', 0)
    overlay_mask = ('class', 'overlay-mask', 0)

    def is_paid_page(self):
        self.element.is_element_exist(self.paid_feeds)

    def is_paid_content_page(self):
        self.element.is_element_exist(self.overlay_mask)
