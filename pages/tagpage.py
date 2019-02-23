from pages.basepage import BasePage
import re

class TagPage(BasePage):
    tag_search_result = ('css', '.tag-search-result', 0)  
    upload_button = ('class', 'upload-btn', 0) #tag页面的upload button
    uploadBtn = ('id', 'uploadBtn', 0) #上传页面的upload button
    popularVideoMore = ('class', 'more', 0)
    videoItem = ('class', 'play-link', 0)
    popularPhotoMore = ('class', 'more', 1)
    photoItem = ('class', 'photo-icon', 0)
    recentExperience = ('class', 'more', 2)
    experienceItem = ('class', 'play-link', 0)
    recentContent = ('class', 'more', 3)
    contentItem = ('class', 'play-link', 0) 
    activity_description = ('class', 'event', 0)

    def click_tag_search_result_first_item(self):
        self.element.click(self.tag_search_result)

    def match_tag_page(self):
        current_url = (self.window.get_current_url())
        pattern = re.compile(r'/tags/*')
        result = re.search(pattern, current_url).group()
        if result is None:
            raise AssertionError("URL Don't match")
        else:
            return True
            
    def click_upload_button(self):
        self.element.click(self.upload_button)

    def match_upload_url(self):
        current_url = (self.window.get_current_url())
        pattern = re.compile(r'/upload')
        result = re.search(pattern, current_url).group()
        if result is None:
            raise AssertionError("URL Don't match")
        else:
            return True

    def is_upload_page(self):
        self.element.ElementExist(self.uploadBtn)

    def enter_more_popular_video(self):
        self.element.click(self.popularVideoMore)
    
    def is_more_popular_video_page(self):
        self.element.ElementExist(self.videoItem)
    
    def select_one_video_play(self):
        self.element.click(self.videoItem)

    def enter_more_popular_photo(self):
        self.element.click(self.popularPhotoMore)

    def is_more_popular_photo_page(self):
        self.element.ElementExist(self.photoItem)
    
    def select_one_photo_play(self):
        self.element.click(self.photoItem)

    def enter_more_recent_content(self):
        self.element.click(self.recentContent)
    
    def is_more_recent_content_page(self):
        self.element.ElementExist(self.contentItem)
        
    def select_first_content_play(self):
        self.element.click(self.contentItem)

    def enter_more_recent_experience(self):
        self.element.click(self.recentExperience)
    
    def is_more_recent_experience_page(self):
        self.element.ElementExist(self.experienceItem)
        
    def select_first_experience_play(self):
        self.element.click(self.experienceItem)

    def this_tag_has_activity_description(self):
        self.element.ElementExist(self.activity_description)
        

    
