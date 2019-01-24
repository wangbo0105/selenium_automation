from pages.basepage import BasePage


class Exppage(object):
    exp_slogan = ('class', 'slogan', 0)  # 互动体验首页banner
    load_layer = ('class', 'load-layer', 0)  # 互动体验详情页-exp播放器

    def __init__(self):
        self.base = BasePage()
        self.slogan_name = 'VeeR 全新互动体验'
        self.banner_tab_active = 'active'
        self.Seth_home_href = 'vr/docs/home'

    @staticmethod
    def exp_page_dict():
        item_name = {'立即体验': ('class', 'join-button', 0),
                     '了解更多': ('class', 'ant-btn-primary-ghost', 1),
                     '餐厅全景图案例': ('class', 'banner-tab', 0),
                     'VR故事': ('class', 'banner-tab', 1),
                     'VRlog日记案例': ('class', 'banner-tab', 2),
                     '上传-了解更多': ('class', 'zh-CN', 0),
                     'Seth的VeeR主页': ('class', 'author-profile-link', 0)}
        return item_name

    def click_item(self, name):
        item = Exppage().exp_page_dict()
        self.base.element.click(item[name])

    def is_exp_page(self):
        self.base.window.is_text_in_url('experience')
        _slogan = self.base.element.get_text(self.exp_slogan)
        self.base.element.should_be_equal(self.slogan_name, _slogan)

    def is_exp_detail_page(self):
        self.base.window.is_text_in_url('experiences/')
        self.base.element.is_element_exist(self.load_layer)

    def is_select_banner_tab(self, name):
        item = Exppage().exp_page_dict()
        att = self.base.element.get_attribute(item[name], 'class')
        self.base.element.should_contains(att, self.banner_tab_active)

    def is_Seth_home_page(self):
        _url = self.base.window.get_current_url()
        self.base.element.should_contains(_url, self.Seth_home_href)
