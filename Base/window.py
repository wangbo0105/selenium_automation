from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from Base import current_driver
from urllib.request import unquote
import os


class Window(object):
    @staticmethod
    def driver():
        return current_driver.get()

    def close(self):
        """关闭当前页面"""
        self.driver().close()
        time.sleep(3)

    def get_screenshot(self, targetpath):
        """获取当前屏幕截图并将其保存到目标路径"""
        self.driver().get_screenshot_as_file(targetpath)

    def get_error_screenshot(self):
        cur_path = './Screenshots/'
        now = time.strftime("%Y_%m_%d_%H_%M_%S")
        name = ('%s.png' % now)
        report_path = os.path.join(cur_path, name)
        self.get_screenshot(report_path)

    def get_screenshot_base64(self):
        """获取当前屏幕截图并将其保存为base64"""
        return self.driver().get_screenshot_as_base64()

    def get_window_size(self):
        """获取当前窗口的宽度和高度"""
        self.driver().get_window_size()

    def set_window_size(self, width, height):
        """设置当前浏览器的宽度和高度"""
        self.driver().set_window_size(width, height)

    def maximize_window(self):
        """最大化当前窗口的浏览器窗口"""
        self.driver().maximize_window()

    def minimize_window(self):
        """最小化当前窗口的浏览器窗口"""
        self.driver().minimize_window()

    def get_handle(self):
        """获取当前页面的句柄"""
        handle = self.driver().current_window_handle
        print(handle)
        return handle

    def switch_handle(self):
        """切换到指定的window_name页面"""
        handle = self.driver().current_window_handle
        print(handle)
        handles = self.driver().window_handles
        print(handles)
        for i in handles:
            if i != handle:
                try:
                    self.driver().switch_to.window(i)
                    time.sleep(3)
                    print("切换页面成功")
                except Exception:
                    print("切换页面失败")

    def switch_handles(self, handle):
        """切换到指定的window_name页面"""
        handles = self.driver().window_handles
        self.driver().switch_to.window(handles[handle])
        time.sleep(3)

    def get_title(self):
        """获取窗口标题"""
        try:
            r = self.driver().title
            return r
        except Exception:
            print("获取标题失败，返回'' ")
            return ""

    def get_current_url(self):
        """获取当前url"""
        try:
            r = unquote(self.driver().current_url, encoding='utf-8')
            return r
        except Exception:
            print("获取当前url失败，返回'' ")
            return ''

    def is_url(self, url):
        """判断当前页面是否是预期页面地址"""
        if unquote(self.driver().current_url, encoding='utf-8') == url:
            return True
        else:
            raise AssertionError("'%s' is not current url." % url)

    def is_text_in_url(self, text):
        """判断当前页面url是否包含指定文本"""
        url = unquote(self.driver().current_url, encoding='utf-8')
        if text in url:
            return True
        else:
            raise AssertionError("'%s' is not in current url.'%s'" % (text, url))

    def is_title(self, _title=''):
        """检查标题是否符合预期"""
        if self.driver().title == _title:
            return True
        else:
            raise AssertionError("'%s' not live up to expectations." % _title)

    def is_text_in_title(self, _title=''):
        """检查标题中是否存在指定的文本"""
        if _title in self.driver().title:
            return True
        else:
            raise AssertionError("'%s' is not in current title." % _title)

    def is_alert(self, timeout=3, t=0.5, type='accept'):
        """判断当前页面的alert弹窗"""
        alert = WebDriverWait(self.driver(), timeout, t).until(EC.alert_is_present())
        if alert:
            current_alert = self.driver().switch_to.alert(alert)
            alert_text = current_alert.text
            print(alert_text)
            if type == 'accept':
                current_alert.accept()
            else:
                current_alert.dismiss()
        else:
            print("alert 未弹出！")
