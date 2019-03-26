from pages.basepage import BasePage
import time
import re


class Navigator(BasePage):

    @staticmethod
    def page_dict():
        page_name = {'logo': ('class', 'logo', 0),
                     'search': ('class', 'ant-input', 1),
                     'home': ('class', 'home', 0),
                     'video': ('class', 'ant-menu-item', 1),
                     'photo': ('class', 'ant-menu-item', 2),
                     'experience': ('class', 'ant-menu-item', 3),
                     'blog': ('class', 'ant-menu-item', 4),
                     'store': ('class', 'ant-menu-item', 5),
                     'message': ('class', 'message-box-header', 0),
                     'signup': ('class', 'header-signup', 0),
                     'login': ('class', 'header-login', 0),
                     'user': ('class', 'ant-dropdown-trigger', 0),
                     'upload': ('class', 'upload-btn', 0), }
        return page_name

    def go_page(self, name):
        page = Navigator().page_dict()
        self.element.click(page[name])
        time.sleep(2)

    @staticmethod
    def page_url_regular_dict():
        url_regular = {
            'home': r'(http[s]?://([a-zA-Z0-9]+.\w+\.+[tv]+))',
            'search': r'/search/',
            'photo': r'/photo[s]?.*',
            'video': r'/videos.*',
            'videos': r'/videos/.*',
            'experience': r'/experience[s]?.*',
            'blog': r'/blog/',
            'store': r'(http[s]?://shop([0-9]{9}.taobao.com))',
            'upload': r'/upload',
            'message': r'/messages',
            'paid': r'/paid',
            'contents': r'/contents/'

        }
        return url_regular

    def match_url(self, _regular):
        _url = Navigator().page_url_regular_dict()
        current_url = (self.window.get_current_url())
        pattern = re.compile(_url[_regular])
        result = re.search(pattern, current_url).group()
        if result is None:
            raise AssertionError("URL Don't match")
        else:
            return True

    @staticmethod
    def page_slogan_dict():
        slogan_name = {'home': '环 球 V R 内 容 社 区',
                       'photo': 'VeeR 360 全景图',
                       'video': 'VeeR VR 视频',
                       'experience': 'VeeR 全新互动体验',
                       'blog': ' VeeR VR 博客 ',
                       'upload': '上传360/VR图片或视频',
                       'message': '消息',

                       }
        return slogan_name

    @staticmethod
    def page_slogan_element_dict():
        slogan_ele = {'home': ('class', 'app-des', 0),
                      'photo': ('class', 'slogan', 0),
                      'video': ('class', 'slogan', 0),
                      'experience': ('class', 'slogan', 0),
                      'blog': ('class', 'navbar-brand', 0),
                      'upload': ('class', 'upload-title', 0),
                      'message': ('class', 'inner-page-title', 0),

                      }
        return slogan_ele

    def check_current_page(self, _page):
        _slogan = Navigator().page_slogan_dict()
        _ele = Navigator().page_slogan_element_dict()
        self.element.is_text_in_element(_ele[_page], _slogan[_page])
