from robot.api.deco import keyword
from pages.share import Share


class ShareLibrary(object):
    def __init__(self):
        self.share = Share()

    @keyword
    def click_channels(self, name):
        self.share.click_share_btn()
        self.share.click_channels_item(name)

    @keyword
    def check_channels_results(self, name):
        self.share.check_channels_results(name)

    # @keyword
    # def check_share_link(self, name):
    #     self.share.check_share_link(name)
