from Base import current_driver
import time


class Browser(object):
    def open(self, url):
        """打开浏览器并获取指定url页面"""
        if url != '':
            # self.driver.implicitly_wait(10)  # 隐性等待10s
            current_driver.get().get(url)
        else:
            print('Please enter the correct url')

    def back(self):
        """前往浏览器历史的上个页面"""
        current_driver.get().back()

    def forward(self):
        """前往浏览器历史的下个页面"""
        current_driver.get().forward()

    def refresh(self):
        """刷新当前页面"""
        current_driver.get().refresh()
        time.sleep(3)

    def quit(self):
        """退出浏览器"""
        current_driver.quit()
