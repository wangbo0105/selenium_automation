from pages.basepage import BasePage


class HomePage(BasePage):
    recommended_view_all = ('class', 'view-all', 0)  # 推荐-查看全部
    recommended_container = ('class', 'main-container', 0)  # 推荐container
    recommended_content = ('class', 'title', 1)  # 推荐-第一个作品
    recommended_show_more_btn = ('class', 'show-more', 0)  # 推荐-展开
    photo_player = ('class', 'photo-player', 0)  # photo-player
    video_player = ('class', 'video-player', 0)  # video-player
    collection_info = ('class', 'collection-info', 0)  # collection-info
    experience_player = ('class', 'experience-detail-player', 0)  # experience-detail-player
    wrapper_right = ('class', 'anticon-right', 1)  # 向右翻页
    wrapper_left = ('class', 'anticon-left', 0)  # 向左翻页

    def __init__(self):
        super().__init__()
        self.recommended_content_href = None

    @staticmethod
    def feeds_dict(name):
        item_name = {name: ('xpath', "//h1[text()=\"%s\"]" % name, 0),
                     # name: ('xpath', "//div[@class='content-list-view']/header/a/h1[text()=\"%s\"]" % name, 0),
                     }
        return item_name

    @staticmethod
    def feeds_content_dict(name):
        if name == u'精选互动' or name == 'Featured Experience':
            item_name = {name: ('xpath', "//h1[text()=\"%s\"]/../../div[1]/div/div[1]/div[1]/div[1]" % name, 0)}
        elif name == u'付费专区' or name == 'Top Paid':
            item_name = {name: ('xpath', "//h1[text()=\"%s\"]/../../../div[1]/div/div[1]/a/div[1]" % name, 0)}
        else:
            # item_name = {name: ('xpath', "//h1[text()=\"%s\"]/../../../div[1]/div/div[1]/div[1]/div[1]" % name, 0)}
            item_name = {
                name: ('xpath', "//h1[text=()=\"%s\"]/ancestor::[contains(@class,'content-list-view')]" % name, 0)}
        return item_name

    @staticmethod
    def category_tabs_dict(name):
        item_name = {name: ('xpath', "//a[text()=\"%s\"]/.." % name, 0)}
        return item_name

    @staticmethod
    def get_feeds_item(name):
        item = HomePage().feeds_dict(name)
        return item[name]

    def click_feeds_item(self, name):
        self.element.click(HomePage().get_feeds_item(name))

    @staticmethod
    def get_feeds_content_item(name):
        item = HomePage().feeds_content_dict(name)
        return item[name]

    def click_feeds_content_item(self, name):
        self.element.click(HomePage().get_feeds_content_item(name))

    @staticmethod
    def get_category_tabs_item(name):
        item = HomePage().category_tabs_dict(name)
        return item[name]

    def click_category_tab(self, name):
        self.element.click(HomePage().get_category_tabs_item(name))

    def check_category_page(self, name):
        active = self.element.get_attribute(HomePage().get_category_tabs_item(name), 'class')
        self.element.should_contains(active, 'tabs-tab-active')
        self.window.is_text_in_url(name)

    def recommended_page(self):
        """判断当前页面是推荐主页"""
        self.window.is_text_in_url('recommended')
        self.element.is_element_exist(self.recommended_container)

    def click_recommended_content(self):
        """点击推荐-第一个推荐"""
        self.element.click(self.recommended_content)

    def get_recommended_content_href(self):
        """获取推荐-第一个推荐的链接"""
        self.recommended_content_href = self.element.get_attribute_href(self.recommended_content)

    def recommended_content_detail_page(self):
        """判断是否是推荐-第一个推荐详情页"""
        href = self.recommended_content_href
        self.window.is_text_in_url(href)
        if 'photos' in href:
            self.element.is_element_exist(self.photo_player)
        elif 'videos' in href:
            self.element.is_element_exist(self.video_player)
        elif 'collections' in href:
            self.element.is_element_exist(self.collection_info)
        elif 'experiences' in href:
            self.element.is_element_exist(self.experience_player)
        else:
            raise AttributeError('链接类型异常')
        self.recommended_content_href = None

    def click_recommended_show_more(self):
        """点击推荐-展开"""
        self.element.click(self.recommended_show_more_btn)

    def recommended_show_more(self):
        """判断推荐是否展开更多"""
        self.element.is_element_not_exist(self.recommended_show_more_btn)

    def turning_page(self, _direction):
        if _direction == 'right':
            self.element.click(self.wrapper_right)
        elif _direction == 'left':
            self.element.click(self.wrapper_left)
        else:
            raise AttributeError('arguments error,%s' % _direction)

    def is_turned_right(self):
        self.element.is_element_exist(self.wrapper_left)
