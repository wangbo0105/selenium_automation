from Base.browser import Browser


class JavaScript(Browser):

    def js_scroll(self, x, y):
        """滑动滚动条至指定位置"""
        js = "window.scrollTo(%s,%s)" % x, y
        self.driver.execute_script(js)

    def js_scroll_top(self):
        """滚动到顶部"""
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)

    def js_scroll_end(self, x=0):
        """滚动到底部"""
        js = "window.scrollTo(%s,document.body.scrollHeight)" % x
        self.driver.execute_script(js)
