from services.BrowserLibrary import BrowserLibrary


class Storepage(BrowserLibrary):
    store_tab = ('xpath', '//*[@id="app"]/div/div/header/nav[1]/div/ul/li[6]/a')  # 商城tab

    def go_store_page(self):
        storetab = self.base.findElement(self.store_tab)
        self.base.click(storetab)
        return self
