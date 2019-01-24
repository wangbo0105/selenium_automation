from pages.basepage import BasePage


class StorePage(BasePage):
    store_title = "首页-VeeR商城-淘宝网"  # 商城页面title
    store_tab = ('class', 'nav-item', 0)  # 导航栏-商城

    def is_store_page(self):
        self.window.switch_handle()
        self.window.is_title('首页-VeeR商城-淘宝网')
