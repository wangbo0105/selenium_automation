from robot.api.deco import keyword
from pages.searchpage import Searchpage
import time



class SearchLibrary(object):
    def __init__(self):
        self.search = Searchpage()

    @keyword
    def search_content(self, searchword):
        """点击搜索，输入搜索词，敲击回车，查看搜索结果"""
        self.search.click_search_box()
        self.search.input_searchWord(searchword)
        time.sleep(3)

    @keyword
    def delete_keywords(self):
        """删除搜索词"""
        self.search.delete_keywords()
        
    @keyword
    def switch_tab_tag(self):
        """搜索结果切换到tag的tab"""
        self.search.click_tag_tab()

    @keyword
    def switch_tab(self,tabName):
        """根据传入参数跳转切换所有tab"""
        self.search.select_tab(tabName)

    @keyword
    def check_search_result(self):
        self.search.check_searchResult()

    @keyword
    def check_no_result_page(self):
        # time.sleep(3)
        self.search.check_no_result_page()

    @keyword
    def check_top_content_list(self):
        self.search.has_top_content_list()

    @keyword
    def select_one_content_play(self):
        self.search.click_one_content_play()

    @keyword
    def filter_photo(self):
        self.search.select_photo_filter()
        time.sleep(3)

    @keyword
    def filter_experience(self):
        self.search.select_experience_filter()
        time.sleep(3)

    @keyword
    def filter_all_content(self):
        self.search.select_all_content_filter()
        time.sleep(3)

    @keyword
    def filter_video(self):
        self.search.select_video_filter()
        time.sleep(3)

    @keyword
    def check_this_is_a_video_and_play (self):
        self.search.video_has_duration()
        self.search.click_video()
    
    @keyword
    def check_this_is_a_photo_and_play (self):
        self.search.video_has_duration()
        self.search.click_video()

    @keyword
    def select_one_content_and_play (self):
        self.search.click_one_content()

    @keyword
    def go_back (self):
        self.search.go_back()
  
    @keyword
    def select_one_collection (self):
        self.search.click_collection_search_result_first_item() 

    @keyword
    def select_one_user (self):
        self.search.click_user_search_result_first_item()
    
    
    
    
    

        
    
        
