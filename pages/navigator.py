from pages.basepage import BasePage


class Navigator(BasePage):

    @staticmethod
    def page_dict():
        page_name = {'logo': ('class', 'logo', 0),
                     '搜索': ('class', 'ant-input', 1),
                     '首页': ('class', 'home', 0),
                     '视频': ('class', 'ant-menu-item', 1),
                     '全景图': ('class', 'ant-menu-item', 2),
                     '互动体验': ('class', 'ant-menu-item', 3),
                     '博客': ('class', 'ant-menu-item', 4),
                     '商城': ('class', 'nav-item', 0),
                     '消息': ('class', 'message-box-header', 0),
                     '登录': ('class', 'header-login', 0),
                     '用户': ('class', 'ant-dropdown-trigger', 0),
                     '上传': ('class', 'upload-btn', 0), }
        return page_name

    def go_page(self, name):
        page = Navigator().page_dict()
        self.element.click(page[name])
