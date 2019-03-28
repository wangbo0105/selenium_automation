from pages.basepage import BasePage


class Pagination:

    def __init__(self):
        self.base = BasePage()

    @staticmethod
    def page_item_dict():
        item = {'last_page': ('css', '.pagination li', 0),
                'next_page': ('css', '.pagination li', -1),
                'page_1': ('css', '.pagination li', 1),
                'page_2': ('css', '.pagination li', 2),
                'page_3': ('css', '.pagination li', 3),

                }
        return item

    def get_page_item_dict(self, name):
        item_name = self.page_item_dict()
        return item_name[name]

    def turn_page(self, name):
        self.base.js.js_scroll_end(num=4, sleep=1)
        self.base.element.click(self.get_page_item_dict(name))

    def check_page_active(self, name):
        self.base.js.js_scroll_end(num=3, sleep=1)
        active = self.base.element.get_attribute(self.get_page_item_dict(name), 'class')
        self.base.element.should_contains(active, 'active')
