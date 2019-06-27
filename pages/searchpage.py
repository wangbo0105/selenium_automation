from pages.basepage import BasePage



class Searchpage(BasePage):
    search_box = ('class', 'search-box')  # 搜索框
    search_input = ('id', 'searchInput', 0)  # 搜索词输入框
    search_result = ('class', 'tabs-nav', 0)  # 搜索结果内容容器

    content_tab = ('class', 'tabs-tab', 0) 
    collection_tab = ('class', 'tabs-tab', 1) 
    user_tab = ('class', 'tabs-tab', 2) 
    tag_tab = ('class', 'tabs-tab', 3) # 切换tab到tag

    no_content_img = ('class', 'search-result-empty', 0)
    _container = ('class', 'content-container', 0)  # 搜索结果页面

    top_content_icon = ('class', 'search-hot-tokens', 0)
    topContentItem = ('class', 'hot-token-link', 0)

    duration_icon = ('class', 'duration', 0)
    videoItem = ('class', 'play-overlay', 0)
    contentItem = ('class', 'content-pc-list-box', 0)

    contentFilter = ('class', 'select-type', 0)
    photoFilter = ('class', 'ant-dropdown-menu-item', 0)
    videoFilter = ('class', 'ant-dropdown-menu-item', 0)
    experienceFilter = ('class', 'ant-dropdown-menu-item', 0)

    collectionItem = ('class', 'collection-search-result-box', 0)
    userItem = ('class', 'user-search-result', 0)



    def click_search_box(self):
        self.element.click(self.search_input)

    def input_searchWord(self, searchword):
        # 输入搜索词
        self.element.send_keys(self.search_input, searchword)
        # 点击回车
        self.element.enter(self.search_input)

    def click_tag_tab(self):
        self.element.click(self.tag_tab)

    def delete_keywords(self):
        self.element.double_click(self.search_input)
        self.element.backSpace(self.search_input)

    def check_searchResult(self):
        self.element.is_element_exist(self._container)

    def select_tab(self, tabName):
        if tabName == 'content': 
          self.element.click(self.content_tab),
        elif tabName == 'collection': 
          self.element.click(self.collection_tab),
        elif tabName == 'user': 
          self.element.click(self.user_tab),
        elif tabName == 'tag': 
          self.element.click(self.tag_tab)           

    def check_no_result_page(self):
        self.element.is_element_exist(self.no_content_img)

    def has_top_content_list(self):
        self.element.is_element_exist(self.top_content_icon)
    
    def click_one_content_play(self):
        self.element.click(self.topContentItem)
    
    def select_all_content_filter(self):
        self.element.click(self.contentFilter)
        self.element.click(self.contentFilter)

    def select_video_filter(self):
        self.element.click(self.contentFilter)
        self.element.click(self.videoFilter)

    def select_photo_filter(self):
        self.element.click(self.contentFilter)
        self.element.click(self.photoFilter)

    def select_experience_filter(self):
        self.element.click(self.contentFilter)
        self.element.click(self.experienceFilter)

    def video_has_duration(self):
        self.element.is_element_exist(self.duration_icon)

    def click_video(self):
        self.element.click(self.videoItem)
    
    def click_one_content(self):
        self.element.click(self.contentItem)

    def go_back(self):
        self.browser.back()

    def click_collection_search_result_first_item(self):
        self.element.click(self.collectionItem)
        
    def click_user_search_result_first_item(self):
        self.element.click(self.userItem)



        
