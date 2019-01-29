from Base.element import Element
from Base.browser import Browser
from Base.window import Window
from Base.frame import Frame
from Base.javascript import JavaScript


class BasePage(object):
    def __init__(self):
        self.element = Element()
        self.browser = Browser()
        self.window = Window()
        self.frame = Frame()
        self.js = JavaScript()
        self.url = 'https://stg.veervr.tv/'

    @staticmethod
    def page_dict():
        page_name = {'首页': ('class', 'home', 0),
                     'logo': ('class', 'logo', 0),
                     '全景图': ('class', 'ant-menu-item', 2),
                     '视频': ('class', 'ant-menu-item', 1),
                     '互动体验': ('class', 'ant-menu-item', 3),
                     '博客': ('class', 'ant-menu-item', 4),
                     '商城': ('class', 'nav-item', 0),
                     '消息': ('class', 'message-box-header', 0),
                     '上传': ('class', 'upload-btn', 0),
                     'signup': ('class','header-signup',0),
                     '登录': ('class', 'header-login', 0),
                     '退出登录': ('link_text', '退出', 0),
                     '用户': ('class', 'ant-dropdown-trigger', 0),
                     '设置': ('link_text', '设置', 0),
                     '个人中心': ('link_text', '个人中心', 0),
                     '合辑': ('class', ' tabs-tab', 2),
                     'VR书签': ('class', ' tabs-tab', 3),
                     '关注': ('class', 'following', 0),
                     '喜欢': ('class', ' tabs-tab', 4),
                     '推荐': ('class', 'view-all', 0), }
        return page_name

    def go_page(self, name):
        page = BasePage().page_dict()
        if name in ('个人中心', '我的上传', '设置', '退出登录'):
            self.element.move_to_element(page['用户'])
            self.element.click(page[name])
        elif name in ('VR书签', '合辑', '关注', '喜欢'):
            self.element.move_to_element(page['用户'])
            self.element.click(page['个人中心'])
            self.element.click(page[name])
        else:
            self.element.click(page[name])
