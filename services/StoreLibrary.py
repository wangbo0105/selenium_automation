from robot.api.deco import keyword
from pages.storepage import Storepage
from services.CommonLibrary import CommonLibrary


class StoreLibrary(Storepage):
    cl = CommonLibrary()

    @keyword
    def go_store(self):
        self.cl.goto_page_by_click(self.store_tab)

    @keyword
    def is_store_page(self):
        self.switch_handle()
        self.is_title('首页-VeeR商城-淘宝网')
