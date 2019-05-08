import time

from pages.basepage import BasePage
import re


class ExpPage(BasePage):
    exp_slogan = ('class', 'experience-detail-player', 0)  # 互动体验首页banner
    load_layer = ('class', 'load-layer', 0)  # 互动体验详情页-exp播放器

    banner_tab_active = 'active'
    Seth_home_href = 'vr/docs/home'

    @staticmethod
    def exp_page_dict():
        item_name = {'experience_immediately': ('class', 'join-button', 0),
                     'learn_more': ('class', 'ant-btn-primary-ghost', 1),
                     'restaurant_panorama_case': ('class', 'banner-tab', 0),
                     'VR_story': ('class', 'banner-tab', 1),
                     'VRlog_diary_case': ('class', 'banner-tab', 2),
                     'upload_learn_more': ('class', 'zh-CN', 0),
                     'Seth_veer_page': ('class', 'author-profile-link', 0)}
        return item_name

    def click_item(self, name):
        item = ExpPage().exp_page_dict()
        self.element.click(item[name])

    def match_exp_url(self):
        current_url = (self.window.get_current_url())
        pattern = re.compile(r'/experience[s]?.*')
        result = re.search(pattern, current_url).group()
        if result is None:
            raise AssertionError("URL Don't match")
        else:
            return True

    def is_exp_page(self):
        _slogan = self.element.get_text(self.exp_slogan)
        self.element.should_be_equal(self.slogan_name, _slogan)

    def is_exp_detail_page(self):
        time.sleep(2)
        self.element.is_element_exist(self.load_layer)

    def is_select_banner_tab(self, name):
        item = ExpPage().exp_page_dict()
        att = self.element.get_attribute(item[name], 'class')
        self.element.should_contains(att, self.banner_tab_active)

    def is_Seth_home_page(self):
        _url = self.window.get_current_url()
        self.element.should_contains(_url, self.Seth_home_href)
