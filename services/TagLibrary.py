from robot.api.deco import keyword
from pages.tagpage import TagPage
from services.CommonLibrary import CommonLibrary
import time


class TagLibrary(object):
    def __init__(self):
        self.tag = TagPage()
        self.common = CommonLibrary()

    @keyword
    def enter_tag_page(self):
        time.sleep(3)
        self.tag.click_tag_search_result_first_item()

    @keyword
    def match_tag_page(self):
        self.tag.match_tag_page()

    @keyword
    def select_upload(self):
        self.tag.click_upload_button()

    @keyword
    def match_upload_page(self):
        self.tag.match_upload_url()
        self.tag.is_upload_page()

    @keyword
    def select_popular_video_more(self):
        self.tag.enter_more_popular_video()
        self.tag.is_more_popular_video_page()

    @keyword
    def select_first_video_play(self):
        # self.tag.is_more_popular_video_page()
        self.tag.select_one_video_play()

    @keyword
    def select_popular_photo_more(self):
        self.tag.enter_more_popular_photo()
        self.tag.is_more_popular_photo_page()

    @keyword
    def select_first_photo_play(self):
        self.tag.select_one_photo_play()

    @keyword
    def select_recent_content_more(self):
        self.tag.enter_more_recent_content()
        self.tag.is_more_recent_content_page()
    
    @keyword
    def select_first_content_play(self):
        self.tag.select_first_content_play()

    @keyword
    def select_recent_experience_more(self):
        self.tag.enter_more_recent_experience()
        self.tag.is_more_recent_experience_page()
    
    @keyword
    def select_first_experience_play(self):
        self.tag.select_first_experience_play()

    @keyword
    def check_this_tag_has_activity_description(self):
        self.tag.this_tag_has_activity_description()
        
