from pages.basepage import BasePage


class PhotoPage(BasePage):
    photo_tab = ('class', 'ant-menu-item', 2)  # 导航栏-全景图
    photo_content_1 = ('class', 'photo-card-single', 0)  # 全景图-列表第一个作品
    user_avator = ('class', 'user-avatar', 0)  # content user-avatar
    slogan = ('class', 'slogan', 0)  # 全景图 banner_title
    slogan_name = 'VeeR 360 全景图'  # 全景图 banner标题文本
    featured_tab = ('class', 'tabs-tab', 0)  # 精选tab
    popular_tab = ('class', 'tabs-tab', 1)  # 最热tab
    recent_tab = ('class', 'tabs-tab', 2)  # 最近tab
    tabs_tab_active = 'tabs-tab-active'  # tab选中态
    pagination_item_active = 'active'  # 页标选中态
    pagination_bar_2 = ('css', '.pagination li', 2)  # 翻页bar-页标2
    pagination_bar_btn = ('css', '.pagination li', 4)  # 翻页bar-翻页btn
    photo_player = ('class', 'photo-overlay', 0)  # 照片播放器
    more_image_responsive = ('css', '.image-responsive img', 0)  # 播放详情页 更多作品第一个
    content_title = ('class', 'title', 1)  # photo title

    def __init__(self):
        super().__init__()
        self.photo_src1 = None
        self.photo_src2 = None

    def get_photo_content_user_info(self):
        return self.element.get_attribute_href(self.user_avator)

    def get_photo_content_title(self):
        self.photo_src1 = self.element.get_attribute(self.more_image_responsive, 'alt')

    def click_photo_content_1(self):
        self.element.click(self.photo_content_1)

    def is_photo_page(self):
        self.window.is_text_in_url('photo')
        self.element.is_text_in_element(self.slogan, self.slogan_name)

    def is_photo_detail_page(self):
        self.window.is_text_in_url('photos/')
        self.element.is_element_exist(self.photo_player)
        self.photo_src2 = self.element.get_text(self.content_title)
        self.element.should_be_equal(self.photo_src1, self.photo_src2)
        self.photo_src1 = None
        self.photo_src2 = None

    def click_featured_tab(self):
        self.element.click(self.featured_tab)

    def is_featured_tab(self):
        self.window.is_text_in_url('photo/featured')
        active = self.element.get_attribute(self.featured_tab, 'class')
        self.element.should_contains(active, self.tabs_tab_active)

    def click_popular_tab(self):
        self.element.click(self.popular_tab)

    def is_popular_tab(self):
        self.window.is_text_in_url('photo/popular')
        active = self.element.get_attribute(self.popular_tab, 'class')
        self.element.should_contains(active, self.tabs_tab_active)

    def click_recent_tab(self):
        self.element.click(self.recent_tab)

    def is_recent_tab(self):
        self.window.is_text_in_url('photo/recent')
        active = self.element.get_attribute(self.recent_tab, 'class')
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





