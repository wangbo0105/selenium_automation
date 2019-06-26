from pages.basepage import BasePage
import time


class HomePage(BasePage):
    recommended_item = ('xpath', "//h1[text()='推荐']", 0)
    recommended_container = ('class', 'main-container', 0)  # 推荐container
    recommended_content = ('xpath', '//div[@class="title-name"]/a[@class="title"]', 1)  # 推荐-第一个作品
    recommended_show_more_btn = ('class', 'show-more', 0)  # 推荐-展开
    play_overlay = ('class', 'play-overlay', 0)
    channel_content_href = ('xpath', '//div[@class="cover-bg"]/a', 0)  # 频道-第一个作品
    photo_player = ('class', 'photo-player', 0)  # photo-player
    video_player = ('class', 'video-player', 0)  # video-player
    collection_info = ('class', 'collection-info', 0)  # collection-info
    experience_player = ('class', 'experience-detail-player', 0)  # experience-detail-player
    wrapper_right = ('class', 'right', 0)  # 向右翻页
    wrapper_left = ('class', 'left', 0)  # 向左翻页
    discover = ('class', 'discover', 0)
    channel_title = ('class', 'channel-page-title', 0)

    def __init__(self):
        super().__init__()
        self.content_href = None

    @staticmethod
    def channel_list(name):
        item_name = {name: ('xpath', "//p[contains(text(),\'%s\')]" % name, 0),

                     }
        return item_name[name]

    @staticmethod
    def channel_box_list(name):
        item_name = {name: ('xpath', "//p[contains(text(),\'%s\')]/../../.." % name, 0),

                     }
        return item_name[name]

    def select_channel(self, name):
        self.element.click(self.channel_list(name))
        time.sleep(2)

    def check_current_channel(self, name):
        _selects = self.element.get_attribute(self.channel_box_list(name), 'class')
        self.element.should_contains(_selects, 'active')
        self.element.is_text_in_element(self.channel_title, name)

    def click_recommended_item(self):
        self.element.click(self.recommended_item)

    def recommended_page(self):
        """判断当前页面是推荐主页"""
        self.window.is_text_in_url('recommended')
        self.element.is_element_exist(self.recommended_container)

    def click_recommended_content(self):
        """点击推荐-第一个推荐"""
        self.element.click(self.recommended_content)

    def click_channel_content(self):
        self.element.click(self.play_overlay)

    def get_content_href(self, recommend=True):
        """获取推荐-第一个推荐的链接"""
        if recommend:
            self.content_href = self.element.get_attribute_href(self.recommended_content)
        else:
            self.content_href = self.element.get_attribute_href(self.channel_content_href)

    def content_detail_page(self):
        """判断是否是推荐-第一个推荐详情页"""
        href = self.content_href
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
        self.content_href = None

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

    def is_turned_wrapper(self, item):
        if item == 'right':
            self.element.is_element_exist(self.wrapper_left)
        else:
            self.element.is_element_not_exist(self.wrapper_left)
