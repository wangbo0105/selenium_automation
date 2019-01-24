from pages.basepage import BasePage
import re


class PhotoPage(BasePage):
    photo_tab = ('class', 'ant-menu-item', 2)  # 导航栏-全景图
    photo_content_1 = ('class', 'photo-card-single', 0)  # 全景图-列表第一个作品
    user_avator = ('class', 'user-avatar', 0)  # content user-avatar
    slogan = ('class', 'slogan', 0)  # 全景图 banner_title
    pagination_bar_2 = ('css', '.pagination li', 2)  # 翻页bar-页标2
    pagination_bar_btn = ('css', '.pagination li', 4)  # 翻页bar-翻页btn
    photo_player = ('class', 'photo-overlay', 0)  # 照片播放器
    more_image_responsive = ('css', '.image-responsive img', 0)  # 播放详情页 更多作品第一个
    content_title = ('class', 'title', 1)  # photo title

    slogan_name = 'VeeR 360 全景图'  # 全景图 banner标题文本
    tabs_tab_active = 'tabs-tab-active'  # tab选中态
    pagination_item_active = 'active'  # 页标选中态
    photo_src1 = None
    photo_src2 = None

    @staticmethod
    def photo_page_dict():
        item_name = {'featured': ('class', 'tabs-tab', 0),
                     'popular': ('class', 'tabs-tab', 1),
                     'recent': ('class', 'tabs-tab', 2),
                     '图片作品': ('class', 'photo-card-single', 0), }
        return item_name

    def click_item(self, name):
        item = PhotoPage().photo_page_dict()
        self.element.click(item[name])

    def match_video_url(self):
        current_url = (self.window.get_current_url())
        pattern = re.compile(r'/photo[s/]?.*')
        result = re.search(pattern, current_url).group()
        if result is None:
            raise AssertionError("URL Don't match")
        else:
            return True

    def get_photo_content_user_info(self):
        return self.element.get_attribute_href(self.user_avator)

    def get_photo_content_title(self):
        self.photo_src1 = self.element.get_attribute(self.more_image_responsive, 'alt')

    def is_photo_page(self):
        self.element.is_text_in_element(self.slogan, self.slogan_name)

    def is_photo_detail_page(self):
        self.element.is_element_exist(self.photo_player)

    def is_selected_tab(self, name):
        self.window.is_text_in_url(name)
        item = PhotoPage().photo_page_dict()
        active = self.element.get_attribute(item[name], 'class')
        self.element.should_contains(active, self.tabs_tab_active)

    def click_turn_page_btn(self):
        self.photo_src1 = self.get_photo_content_user_info()
        self.js.js_scroll_end(3, 3)
        self.element.click(self.pagination_bar_2)
        self.photo_src2 = self.get_photo_content_user_info()

    def is_turned_page(self):
        self.js.js_scroll_end(3, 3)
        active = self.element.get_attribute(self.pagination_bar_2, 'class')
        self.element.should_contains(active, self.pagination_item_active)
        self.element.should_not_equal(self.photo_src1, self.photo_src2)
        self.photo_src1 = None
        self.photo_src2 = None

    def click_more_photo(self):
        self.element.click(self.more_image_responsive)

    def is_more_photo_page(self):
        self.photo_src2 = self.element.get_text(self.content_title)
        self.element.should_be_equal(self.photo_src1, self.photo_src2)
        self.photo_src1 = None
        self.photo_src2 = None
