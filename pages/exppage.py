from services.BrowserLibrary import BrowserLibrary


class Exppage(BrowserLibrary):
    exp_tab = ('xpath', '//*[@id="app"]/div/div/header/nav[1]/div/ul/li[4]/a')  # 互动体验tab
    learn_more_1 = ('xpath', '//*[@id="app"]/div/div/div/div[2]/div/div[2]/div[1]/button')  # 了解更多第一个

    def go_exp_page(self):
        exptab = self.base.findElement(self.exp_tab)
        self.base.click(exptab)
        return self

    def go_exp_detail_page(self):
        learn_more_1 = self.base.findElement(self.learn_more_1)
        self.base.click(learn_more_1)
        return self

