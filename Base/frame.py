from Base import current_driver
from Base.element import Element


class Frame(object):
    @staticmethod
    def driver():
        return current_driver.get()

    def switch_frame(self, id_index_locator):
        """切换frame"""
        try:
            if isinstance(id_index_locator, int):  # index从0开始，传入整型参数即判定为用index定位
                self.driver().switch_to.frame(id_index_locator)
            elif isinstance(id_index_locator, str):  # 传入str参数则判定为用id/name定位
                self.driver().switch_to.frame(id_index_locator)
            elif isinstance(id_index_locator,
                            tuple):  # WebElement对象，即用find_element系列方法所取得的对象，我们可以用tag_name、xpath等来定位frame对象
                ele = Element().findElement(id_index_locator)
                self.driver().switch_to.frame(ele)
        except Exception:
            print("frame切换异常")

    def back_frame(self):
        """返回父级frame"""
        self.driver().switch_to.parent_frame()

    def quit_frame(self):
        """退出frame"""
        self.driver().switch_to.default_content()
