from robot.api.deco import keyword
from pages.storepage import StorePage


class StoreLibrary(object):

    def __init__(self):
        self.store = StorePage()

    @keyword
    def is_store_page(self):
        self.store.is_store_page()
