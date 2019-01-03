from robot.api.deco import keyword
from pages.storepage import Storepage


class StoreLibrary(Storepage):
    @keyword
    def go_store(self):
        self.go_store_page()
