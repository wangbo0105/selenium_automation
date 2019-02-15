from pages.basepage import BasePage


class HomePage(BasePage):
    home_tab = ('class', 'home', 0)  # 首页tab
    veer_logo = ('class', 'logo', 0)  # veer-logo
    veer_mark_text = ('class', 'app-des', 0)  # 首页banner-title
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
    recommended_content_href = None

    def __init__(self):
        super().__init__()
        self.recommended_content_href = None

    @staticmethod
    def feeds_dict(name):
        item_name = {name: ('xpath', "//h1[text()=\"%s\"]" % name, 0,),
                     }
        return item_name

    @staticmethod
    def get_item(name):
        item = HomePage().feeds_dict(name)
        return item[name]

    def click_item(self, name):
        self.element.click(HomePage().get_item(name))

    def home_page(self):
        self.window.is_url(self.url)
        self.element.is_element_exist(self.veer_mark_text)

    def click_recommended_view_all(self):
        """点击推荐-查看全部"""
        self.element.click(self.recommended_view_all)

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

    def turning_page_right(self):
        self.element.click(self.wrapper_right)

    def turned_right_checked(self):
        self.element.is_element_exist(self.wrapper_left)

    def turning_page_left(self):
        self.element.click(self.wrapper_left)
