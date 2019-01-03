from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchAttributeException
import threading
import time


# noinspection PyBroadException
class Base(object):
    """基于原生的selenium进行2次封装"""
    _instance_lock = threading.Lock()

    def __init__(self, browser='chrome'):
        """
        初始化selenium webdriver，使用chrome作为默认的webdriver
        :param browser: 要打开的浏览器类型
        """
        global driver
        self.timeout = 10
        self.t = 0.5
        option_chrome = webdriver.ChromeOptions()
        option_chrome.add_argument(
            'disable-infobars')  # 关闭“Chrome正处于软件的自动控制之下”信息栏
        option_chrome.add_argument('kiosk')  # Mac 全屏
        option_chrome.add_argument('maximized')  # Windows 全屏

        if browser == 'chrome':
            driver = webdriver.Chrome(chrome_options=option_chrome)
        elif browser == 'firefox':
            driver = webdriver.Firefox()
        elif browser == 'safari':
            driver = webdriver.Safari()
        try:
            self.driver = driver
        except Exception:
            raise NameError("没有找到%s浏览器,你可以输入'firefox','chrome','safari'." % browser)

    def __new__(cls, *args, **kwargs):
        if not hasattr(Base, "_instance"):
            with Base._instance_lock:
                if not hasattr(Base, "_instance"):
                    Base._instance = object.__new__(cls)
        return Base._instance

    def findElement(self, element):
        """
        封装元素定位的方法
        :param index:
        :param element: 一个具有(标识符类型、值)格式的集合，例如('id'、'用户名')
        :return: ele
        """
        try:
            type = element[0]
            value = element[1]

            if type == 'id' or type == 'ID' or type == 'Id':
                ele = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element_by_id(value))
            elif type == 'name' or type == 'NAME' or type == 'Name':
                ele = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element_by_name(value))
            elif type == 'class' or type == 'CLASS' or type == 'Class':
                ele = WebDriverWait(self.driver, self.timeout, self.t).until(
                    lambda x: x.find_element_by_class_name(value))
            elif type == 'xpath' or type == 'XPATH' or type == 'Xpath':
                # xpath格式：element = ('xpath', ".//*[@id='kw']")
                ele = WebDriverWait(self.driver, self.timeout, self.t).until(
                    lambda x: x.find_element_by_xpath(value))
            elif type == 'css' or type == 'CSS' or type == 'Css':
                ele = WebDriverWait(self.driver, self.timeout, self.t).until(
                    lambda x: x.find_element_by_css_selector(value))
            elif type == 'link_text' or type == 'LINK_TEXT' or type == 'Link_text':
                ele = WebDriverWait(self.driver, self.timeout, self.t).until(
                    lambda x: x.find_element_by_link_text(value))
            elif type == 'partial_link_text' or type == 'Partial_Link_Text' or type == 'Partial_link_text':
                ele = WebDriverWait(self.driver, self.timeout, self.t).until(
                    lambda x: x.find_element_by_partial_link_text(value))
            elif type == 'tag_name' or type == 'TAG_NAME' or type == 'Tag_name':
                ele = WebDriverWait(self.driver, self.timeout, self.t).until(
                    lambda x: x.find_element_by_tag_name(value))
            else:
                raise NameError('请更正函数参数中的类型')
        except Exception:
            raise ValueError('没有发现这种元素:' + str(element))
        return ele

    def findElements(self, element):
        """

        :param element: 是一个具有(标识符类型、值)格式的集合，例如('id'、'用户名')
        :return: ele
        """
        try:
            type = element[0]
            value = element[1]
            index = element[2]
            if type == 'id' or type == 'ID' or type == 'Id':
                ele = WebDriverWait(self.driver, self.timeout, self.t).until(
                    lambda x: x.find_elements_by_id(value)[index])
                # ele = self.driver.find_elements_by_id(value)
            elif type == 'name' or type == 'NAME' or type == 'Name':
                ele = WebDriverWait(self.driver, self.timeout, self.t).until(
                    lambda x: x.find_elements_by_name(value)[index])
            elif type == 'class' or type == 'CLASS' or type == 'Class':
                ele = WebDriverWait(self.driver, self.timeout, self.t).until(
                    lambda x: x.find_elements_by_class_name(value)[index])
            elif type == 'xpath' or type == 'XPATH' or type == 'Xpath':
                ele = WebDriverWait(self.driver, self.timeout, self.t).until(
                    lambda x: x.find_elements_by_xpath(value))
            elif type == 'css' or type == 'CSS' or type == 'Css':
                ele = WebDriverWait(self.driver, self.timeout, self.t).until(
                    lambda x: x.find_elements_by_css_selector(value)[index])
            elif type == 'link_text' or type == 'LINK_TEXT' or type == 'Link_text':
                ele = WebDriverWait(self.driver, self.timeout, self.t).until(
                    lambda x: x.find_elements_by_link_text(value)[index])
            elif type == 'partial_link_text' or type == 'Partial_Link_Text' or type == 'Partial_link_text':
                ele = WebDriverWait(self.driver, self.timeout, self.t).until(
                    lambda x: x.find_elements_by_partial_link_text(value)[index])
            elif type == 'tag_name' or type == 'TAG_NAME' or type == 'Tag_name':
                ele = WebDriverWait(self.driver, self.timeout, self.t).until(
                    lambda x: x.find_elements_by_tag_name(value)[index])
            else:
                raise NameError('请更正函数参数中的类型')
        except Exception:
            raise ValueError('没有发现这种元素:' + str(element))
        return ele

    def open(self, url):
        """打开浏览器并获取指定url页面"""
        if url != '':
            # self.driver.implicitly_wait(10)  # 隐性等待10s
            self.driver.get(url)
        else:
            print('Please enter the correct url')

    def back(self):
        """前往浏览器历史的上个页面"""
        self.driver.back()

    def forward(self):
        """前往浏览器历史的下个页面"""
        self.driver.forward()

    def refresh(self):
        """刷新当前页面"""
        self.driver.refresh()
        time.sleep(3)

    def close(self):
        """关闭当前页面"""
        self.driver.close()
        time.sleep(3)

    def quit(self):
        """退出浏览器"""
        self.driver.quit()

    def get_screenshot(self, targetpath):
        """获取当前屏幕截图并将其保存到目标路径"""
        self.driver.get_screenshot_as_file(targetpath)

    def get_screenshot_base64(self):
        """获取当前屏幕截图并将其保存为base64"""
        return self.driver.get_screenshot_as_base64()

    def get_window_size(self):
        """获取当前窗口的宽度和高度"""
        self.driver.get_window_size()

    def set_window_size(self, width, height):
        """设置当前浏览器的宽度和高度"""
        self.driver.set_window_size(width, height)

    def maximize_window(self):
        """最大化当前窗口的浏览器窗口"""
        self.driver.maximize_window()

    def minimize_window(self):
        """最小化当前窗口的浏览器窗口"""
        self.driver.minimize_window()

    @staticmethod
    def click(ele):
        """单击页面元素，如按钮、图像、链接等"""
        ActionChains(driver).click(ele).perform()
        time.sleep(5)

    @staticmethod
    def double_click(ele):
        """双击页面元素"""
        ActionChains(driver).double_click(ele).perform()

    @staticmethod
    def move_to_element(ele):
        """鼠标悬停操作"""
        ActionChains(driver).move_to_element(ele).perform()

    @staticmethod
    def drag_element(ele, x, y):
        """鼠标拖动元素，x,y为水平纵向拖动的相对距离"""
        ActionChains(driver).click_and_hold(ele).perform()  # 长按元素
        try:
            ActionChains(driver).drag_and_drop_by_offset(ele, x, y).perform()
        except Exception:
            print('元素拖动出现异常')

    @staticmethod
    def send_keys(ele, text=''):
        """输入文本内容"""
        ele.send_keys(text)

    @staticmethod
    def clear(ele):
        """清除文本内容"""
        ele.clear()

    @staticmethod
    def enter(ele):
        """键盘操作回车"""
        ele.send_keys(Keys.RETURN)

    @staticmethod
    def backSpace(ele):
        """键盘操作删除"""
        ele.send_keys(Keys.BACKSPACE)

    @staticmethod
    def space(ele):
        """键盘操作空格"""
        ele.send_keys(Keys.SPACE)

    def get_title(self):
        """获取窗口标题"""
        try:
            r = self.driver.title
            return r
        except Exception:
            print("获取标题失败，返回'' ")
            return ""

    def get_current_url(self):
        """获取当前url"""
        try:
            r = self.driver.current_url
            return r
        except Exception:
            print("获取当前url失败，返回'' ")
            return ''

    @staticmethod
    def get_text(ele):
        """获取web元素的文本"""
        try:
            r = ele.text
            return r
        except Exception:
            print("获取text失败，返回'' ")
            return ""

    @staticmethod
    def get_attribute(ele, name):
        """获取元素属性的属性值"""
        try:
            return ele.get_attribute(name)
        except NoSuchAttributeException as e:
            print("获取%s属性失败，返回'%s' " % name, e)
            return ""

    def isElementExist(self, element):
        """检查元素是否存在"""
        try:
            self.findElement(element)
            return True
        except Exception:
            return False

    def isElementExist2(self, elements):
        """检查元素是否存在"""
        eles = self.findElements(elements)
        n = len(eles)
        if n == 0:
            return False
        elif n == 1:
            return True
        else:
            print("定位到元素的个数：%s" % n)
            return True

    def is_url(self, url):
        """判断当前页面是否是预期页面地址"""
        return self.driver.current_url == url

    def is_text_in_url(self, text):
        """判断当前页面url是否包含指定文本"""
        return text in self.driver.current_url

    def is_title(self, _title=''):
        """检查标题是否符合预期"""
        try:
            result = WebDriverWait(self.driver, self.driver.timeout, self.t).until(EC.title_is(_title))
            return result
        except Exception:
            return False

    def is_text_in_title(self, _title=''):
        """检查标题中是否存在指定的文本"""
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_contains(_title))
            return result
        except Exception:
            return False

    def is_text_in_element(self, element, _text=''):
        """检查某个元素中是否存在指定的文本"""
        if not isinstance(element, tuple):
            print('locator参数类型错误，必须传元祖类型：loc = ("id", "value1")')
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(
                EC.text_to_be_present_in_element(element, _text))
            return result
        except Exception:
            return False

    def is_value_in_element(self, element, _value=''):
        """检查元素是否是指定类型，返回bool值, value为空字符串，返回Fasle"""
        if not isinstance(element, tuple):
            print('locator参数类型错误，必须传元祖类型：loc = ("id", "value1")')
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(
                EC.text_to_be_present_in_element_value(element, _value))
            return result
        except Exception:
            return False

    def is_alert(self, timeout=3, type='accept'):
        """判断当前页面的alert弹窗"""
        alert = WebDriverWait(self.driver, timeout, self.t).until(EC.alert_is_present())
        if alert:
            current_alert = self.driver.switch_to.alert(alert)
            alert_text = current_alert.text
            print(alert_text)
            if type == 'accept':
                current_alert.accept()
            else:
                current_alert.dismiss()
        else:
            print("alert 未弹出！")

    @staticmethod
    def select_by_index(ele, index=0):
        """<select>标签适用，下拉选择框的选择，通过索引,index是索引第几个，从0开始，默认选第一个"""
        Select(ele).select_by_index(index)

    @staticmethod
    def select_by_value(ele, value):
        """<select>标签适用，下拉选择框的选择，通过value属性定位"""
        Select(ele).select_by_value(value)

    @staticmethod
    def select_by_text(ele, text):
        """<select>标签适用，下拉选择框的选择，通过文本值定位"""
        Select(ele).select_by_visible_text(text)

    def switch_frame(self, id_index_locator):
        """切换frame"""
        try:
            if isinstance(id_index_locator, int):  # index从0开始，传入整型参数即判定为用index定位
                self.driver.switch_to.frame(id_index_locator)
            elif isinstance(id_index_locator, str):  # 传入str参数则判定为用id/name定位
                self.driver.switch_to.frame(id_index_locator)
            elif isinstance(id_index_locator,
                            tuple):  # WebElement对象，即用find_element系列方法所取得的对象，我们可以用tag_name、xpath等来定位frame对象
                ele = self.findElement(id_index_locator)
                self.driver.switch_to.frame(ele)
        except Exception:
            print("frame切换异常")

    def back_frame(self):
        """返回父级frame"""
        self.driver.switch_to.parent_frame()

    def quit_frame(self):
        """退出frame"""
        self.driver.switch_to.default_content()

    def get_handle(self):
        """获取当前页面的句柄"""
        handle = self.driver.current_window_handle
        print(handle)
        return handle

    def switch_handle(self):
        """切换到指定的window_name页面"""
        handle = self.driver.current_window_handle
        print(handle)
        handles = self.driver.window_handles
        print(handles)
        for i in handles:
            if i != handle:
                try:
                    self.driver.switch_to.window(i)
                    time.sleep(3)
                    print("切换页面成功")
                except Exception:
                    print("切换页面失败")

    def switch_handles(self, handle):
        """切换到指定的window_name页面"""
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[handle])
        time.sleep(3)

    # def js_focus_element(self, ele):
    #     """聚焦元素"""
    #     self.driver.execute_script("arguments[0].scrollIntoView();", ele)

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


if __name__ == '__main__':
    pass
