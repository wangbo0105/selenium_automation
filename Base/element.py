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

    def findElements(self, element):
        """
        捕获元素，捕获到则返回ele对象，未捕获到则抛出异常提示
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
                    lambda x: x.find_element_by_link_text(value))
            elif type == 'partial_link_text' or type == 'Partial_Link_Text' or type == 'Partial_link_text':
                ele = WebDriverWait(self.driver(), self.timeout, self.t).until(
                    lambda x: x.find_elements_by_partial_link_text(value)[index])
            elif type == 'tag_name' or type == 'TAG_NAME' or type == 'Tag_name':
                ele = WebDriverWait(self.driver(), self.timeout, self.t).until(
                    lambda x: x.find_elements_by_tag_name(value)[index])
            else:
                raise NameError('请更正函数参数中的类型')
        except Exception:
            raise ValueError('没有发现这种元素:' + str(element))
        return ele

    def check_Element(self, element):
        """
        捕获元素，捕获到则返回ele对象，未捕获到则返回False，用于check元素
        :param element: 是一个具有(标识符类型、值)格式的集合，例如('id'、'用户名')
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
                    lambda x: x.find_element_by_link_text(value))
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
            return False

    def click(self, ele):
        """单击页面元素，如按钮、图像、链接等"""
        ActionChains(self.driver()).click(ele).perform()
        time.sleep(3)

    def double_click(self, ele):
        """双击页面元素"""
        ActionChains(self.driver()).double_click(ele).perform()

    def move_to_element(self, ele):
        """鼠标悬停操作"""
        ActionChains(self.driver()).move_to_element(ele).perform()

    def drag_element(self, ele, x, y):
        """鼠标拖动元素，x,y为水平纵向拖动的相对距离"""
        ActionChains(self.driver()).click_and_hold(ele).perform()  # 长按元素
        try:
            ActionChains(self.driver()).drag_and_drop_by_offset(ele, x, y).perform()
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

    def get_text(self, element):
        """获取web元素的文本"""
        try:
            r = self.findElements(element).text
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
        if self.check_Element(element):
            return True
        else:
            return False

    def is_element_not_exist(self, element):
        """断言方法检查元素不存在"""
        if self.check_Element(element):
            raise AssertionError("'%s' existed." % element)
        else:
            return True

    def ElementNotExist(self, element):
        """检查元素不存在"""
        if self.check_Element(element):
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
