from Base import current_driver
from Base.element import Element
import time


class JavaScript(object):
    @staticmethod
    def driver():
        return current_driver.get()

    def js_scroll(self, x, y):
        """滑动滚动条至指定位置"""
        js = "window.scrollTo(%s,%s)" % (x, y)
        self.driver().execute_script(js)

    def js_scroll_ele(self, ele):
        """滑动滚动条至指定元素"""
        target = Element().findElements(ele)
        self.driver().execute_script("arguments[0].scrollIntoView();", target)  # 拖动到可见的元素去

    def js_scroll_top(self):
        """滚动到顶部"""
        js = "window.scrollTo(0,0)"
        self.driver().execute_script(js)

    def js_scroll_end(self, num=1, sleep=0, x=0):
        """滚动到底部"""
        js = "window.scrollTo(%s,document.body.scrollHeight)" % x
        i = 0
        while i < num:
            self.driver().execute_script(js)
            i += 1
            time.sleep(sleep)
