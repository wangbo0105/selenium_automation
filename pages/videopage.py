from pages.basepage import BasePage


class VideoPage(BasePage):
    more_video_href = None

    @staticmethod
    def video_page_dict():
        item_name = {'video_content': ('class', 'play-overlay', 0),
                     'more_video_href': ('xpath', "//*[@class='play-overlay']/a", 0),
                     'video_player': ('class', 'video-player', 0), }
        return item_name

    @staticmethod
    def get_item(name):
        item = VideoPage().video_page_dict()
        return item[name]

    def click_item(self, name):
        self.element.click(VideoPage().get_item(name))

    def is_video_detail_page(self):
        self.element.is_element_exist(VideoPage().get_item('video_player'))

    def get_more_video_content_href(self):
        self.more_video_href = self.element.get_attribute_href(VideoPage().get_item('more_video_href'))

    def is_more_video_page(self):
        current_url = self.window.get_current_url()
        self.element.should_contains(current_url, self.more_video_href)
        self.element.is_element_exist(VideoPage().get_item('video_player'))
