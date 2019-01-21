from pages.basepage import BasePage


class Exppage(object):
    exp_tab = ('class', 'ant-menu-item', 3)  # 导航栏-互动体验
    learn_more_1 = ('class', 'ant-btn-primary-ghost', 1)  # 互动体验-了解更多
    load_layer = ('class', 'load-layer', 0)  # 互动体验详情页-exp播放器

    def __init__(self):
        self.base = BasePage()

    def click_learn_more_btn(self):
        self.base.element.click(self.learn_more_1)

    def is_exp_page(self):
        self.base.window.is_text_in_url('experience')
        self.base.element.is_element_exist(self.learn_more_1)

    def is_exp_detail_page(self):
        self.base.window.is_text_in_url('experiences/')
        self.base.element.is_element_exist(self.load_layer)
