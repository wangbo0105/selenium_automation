from pages.basepage import BasePage
import re


class VideoPage(BasePage):
    video_tab = ('class', 'ant-menu-item', 1)  # 导航栏-视频
    slogan = ('class', 'slogan', 0)  # 精选视频banner-标题
    video_player = ('class', 'video-player', 0)  # 精选视频播放详情页-video_player
    video_more_content_href = ('class', 'title', 6)  # 精选视频 更多作品第一个链接

    slogan_name = 'VeeR VR 视频'
    more_video_href = None

    def match_video_url(self):
        current_url = (self.window.get_current_url())
        pattern = re.compile(r'/videos[/]?.*')
        result = re.search(pattern, current_url).group()
        if result is None:
            raise AssertionError("URL Don't match")
        else:
            return True

    @staticmethod
    def video_page_dict():
        item_name = {'视频作品': ('class', 'play-overlay', 0),
                     '更多视频': ('class', 'title', 6), }
        return item_name

    def click_item(self, name):
        item = VideoPage().video_page_dict()
        self.element.click(item[name])

    def is_video_page(self):
        self.element.is_text_in_element(self.slogan, self.slogan_name)

    def is_video_detail_page(self):
        self.element.is_element_exist(self.video_player)

    def get_more_video_content_href(self):
        self.more_video_href = self.element.get_attribute_href(self.video_more_content_href)

    def is_more_video_page(self):
        current_url = self.window.get_current_url()
        self.element.should_contains(current_url, self.more_video_href)
        self.element.is_element_exist(self.video_player)
