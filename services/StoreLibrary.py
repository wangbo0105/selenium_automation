from robot.api.deco import keyword
from pages.storepage import Storepage


class StoreLibrary(object):

    def __init__(self):
        self.store = Storepage()

    @keyword
    def is_store_page(self):
        self.store.is_store_page()
