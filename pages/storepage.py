from pages.basepage import BasePage


class Storepage(object):
    store_title = "首页-VeeR商城-淘宝网"  # 商城页面title
    store_tab = ('class', 'nav-item', 0)  # 导航栏-商城

    def __init__(self):
        self.base = BasePage()

    def is_store_page(self):
        self.base.window.switch_handle()
        self.base.window.is_title('首页-VeeR商城-淘宝网')
