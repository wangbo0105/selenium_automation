from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchAttributeException
from Base import current_driver
import time


class Element(object):
    timeout = 10
    t = 0.5

    @staticmethod
    def driver():
        return current_driver.get()

    def findElements(self, element, raiseOnNotFound='yes'):
        """
        捕获元素，捕获到则返回ele对象，未捕获到则抛出异常提示
        :param raiseOnNotFound:
        :param element: 是一个具有(标识符类型、值、索引)格式的集合，例如('id'，'用户名'， 0)
        :return: ele
        """
        try:
            type = element[0]
            value = element[1]
            index = element[2]
            if type == 'id' or type == 'ID' or type == 'Id':
                ele = WebDriverWait(self.driver(), self.timeout, self.t).until(
                    lambda x: x.find_elements_by_id(value)[index])
            elif type == 'name' or type == 'NAME' or type == 'Name':
                ele = WebDriverWait(self.driver(), self.timeout, self.t).until(
                    lambda x: x.find_elements_by_name(value)[index])
            elif type == 'class' or type == 'CLASS' or type == 'Class':
                ele = WebDriverWait(self.driver(), self.timeout, self.t).until(
                    lambda x: x.find_elements_by_class_name(value)[index])
            elif type == 'xpath' or type == 'XPATH' or type == 'Xpath':
                ele = WebDriverWait(self.driver(), self.timeout, self.t).until(
                    lambda x: x.find_elements_by_xpath(value))
            elif type == 'css' or type == 'CSS' or type == 'Css':
                ele = WebDriverWait(self.driver(), self.timeout, self.t).until(
                    lambda x: x.find_elements_by_css_selector(value)[index])
            elif type == 'link_text' or type == 'LINK_TEXT' or type == 'Link_text':
                ele = WebDriverWait(self.driver(), self.timeout, self.t).until(
                    lambda x: x.find_element_by_link_text(value)[index])
            elif type == 'partial_link_text' or type == 'Partial_Link_Text' or type == 'Partial_link_text':
                ele = WebDriverWait(self.driver(), self.timeout, self.t).until(
                    lambda x: x.find_elements_by_partial_link_text(value)[index])
            elif type == 'tag_name' or type == 'TAG_NAME' or type == 'Tag_name':
                ele = WebDriverWait(self.driver(), self.timeout, self.t).until(
                    lambda x: x.find_elements_by_tag_name(value)[index])
            else:
                raise NameError('请更正函数参数中的类型')
            return ele
        except:
            if raiseOnNotFound:
                raise ValueError('没有发现这种元素:' + str(element))
            else:
                return False

    def click(self, element):
        """单击页面元素，如按钮、图像、链接等"""
        ActionChains(self.driver()).click(self.findElements(element)).perform()

    def double_click(self, element):
        """双击页面元素"""
        ActionChains(self.driver()).double_click(self.findElements(element)).perform()

    def move_to_element(self, element):
        """鼠标悬停操作"""
        ActionChains(self.driver()).move_to_element(self.findElements(element)).perform()

    def drag_element(self, element, x, y):
        """鼠标拖动元素，x,y为水平纵向拖动的相对距离"""
        ActionChains(self.driver()).click_and_hold(self.findElements(element)).perform()  # 长按元素
        try:
            ActionChains(self.driver()).drag_and_drop_by_offset(self.findElements(element), x, y).perform()
        except Exception:
            print('元素拖动出现异常')

    def send_keys(self, element, text=''):
        """输入文本内容"""
        self.findElements(element).send_keys(text)

    def clear(self, element):
        """清除文本内容"""
        self.findElements(element).clear()

    def enter(self, element):
        """键盘操作回车"""
        self.findElements(element).send_keys(Keys.ENTER)

    def backSpace(self, element):
        """键盘操作删除"""
        self.findElements(element).send_keys(Keys.BACKSPACE)

    def space(self, element):
        """键盘操作空格"""
        self.findElements(element).send_keys(Keys.SPACE)

    def get_text(self, element):
        """获取web元素的文本"""
        try:
            r = self.findElements(element).text
            return r
        except Exception:
            print("获取text失败，返回'' ")
            return ""

    def get_attribute(self, element, name):
        """获取元素属性的属性值"""
        try:
            return self.findElements(element).get_attribute(name)
        except NoSuchAttributeException as e:
            print("获取%s属性失败，返回'%s' " % name, e)
            return ""

    def get_attribute_href(self, element, name='href'):
        """获取元素属性的href属性值"""
        try:
            return self.findElements(element).get_attribute(name)
        except NoSuchAttributeException as e:
            print("获取%s属性失败，返回'%s' " % name, e)
            return ""

    def is_input_text(self, element, value, _text):
        """检查某个元素中是否存在输入的文本"""
        if self.findElements(element).get_attribute(value) == _text:
            return True
        else:
            raise AssertionError("'%s' is not in current element." % _text)

    def is_element_exist(self, element):
        """断言方法检查元素存在"""
        if self.findElements(element):
            return True
        else:
            raise AssertionError("'%s' is not exist." % element)

    def ElementExist(self, element):
        """检查元素存在"""
        if self.findElements(element, False):
            return True
        else:
            return False

    def is_element_not_exist(self, element):
        """断言方法检查元素不存在"""
        if self.findElements(element, False) == False:
            return True
        else:
            raise AssertionError("'%s' existed." % element)

    def ElementNotExist(self, element):
        """检查元素不存在"""
        if self.findElements(element, False):
            return False
        else:
            return True

    def is_text_in_element(self, element, _text=''):
        """断言方法检查某个元素中是否存在指定的文本"""
        if self.findElements(element).text == _text:
            return True
        else:
            raise AssertionError("'%s' is not in current element." % _text)

    @staticmethod
    def should_contains(str1, str2):
        """断言方法检查某个字符串是否包含另一个字符串"""
        if str2 in str1:
            return True
        else:
            raise AssertionError("Don't match")

    @staticmethod
    def should_be_equal(str1, str2):
        """断言方法检查两个字符串是否相等"""
        if str1 == str2:
            return True
        else:
            raise AssertionError("Don't match")

    @staticmethod
    def should_not_equal(str1, str2):
        """断言方法检查两个字符串是否相等"""
        if str1 != str2:
            return True
        else:
            raise AssertionError("Don't match")

    def select_by_index(self, element, index=0):
        """<select>标签适用，下拉选择框的选择，通过索引,index是索引第几个，从0开始，默认选第一个"""
        Select(self.findElements(element)).select_by_index(index)

    def select_by_value(self, element, value):
        """<select>标签适用，下拉选择框的选择，通过value属性定位"""
        Select(self.findElements(element)).select_by_value(value)

    def select_by_text(self, element, text):
        """<select>标签适用，下拉选择框的选择，通过文本值定位"""
        Select(self.findElements(element)).select_by_visible_text(text)
