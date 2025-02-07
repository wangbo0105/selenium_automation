import json

from Base import current_driver
import time


class Browser(object):
    @staticmethod
    def driver():
        return current_driver.get()

    def open(self, url):
        """打开浏览器并获取指定url页面"""
        if url != '':
            # self.driver.implicitly_wait(10)  # 隐性等待10s
            self.driver().get(url)
        else:
            print('Please enter the correct url')

    def back(self):
        """前往浏览器历史的上个页面"""
        self.driver().back()

    def forward(self):
        """前往浏览器历史的下个页面"""
        self.driver().forward()

    def refresh(self):
        """刷新当前页面"""
        self.driver().refresh()
        time.sleep(3)

    @staticmethod
    def quit():
        """退出浏览器"""
        current_driver.quit()

    def get_cookies(self):
        cookies = self.driver().get_cookies()
        with open("cookies.json", "w") as fp:
            json.dump(cookies, fp)

    def add_cookies(self):
        with open("cookies.json", "r") as fp:
            cookies = json.load(fp)
            for cookie in cookies:
                self.driver().add_cookie(cookie)
