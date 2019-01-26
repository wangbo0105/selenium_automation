from pages.basepage import BasePage


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
                     'store': ('class', 'nav-item', 0),
                     'message': ('class', 'message-box-header', 0),
                     'login': ('class', 'header-login', 0),
                     'user': ('class', 'ant-dropdown-trigger', 0),
                     'upload': ('class', 'upload-btn', 0), }
        return page_name

    def go_page(self, name):
        page = Navigator().page_dict()
        self.element.click(page[name])
