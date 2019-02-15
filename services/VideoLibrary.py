from robot.api.deco import keyword
from pages.videopage import VideoPage
from services.CommonLibrary import CommonLibrary


class VideoLibrary(object):
    def __init__(self):
        self.video = VideoPage()
        self.common = CommonLibrary()

    @keyword
    def video_click_item(self, name):
        self.video.click_item(name)

    @keyword
    def should_be_video_detail_page(self):
        self.common.url_should_be_matching('videos')
        self.video.is_video_detail_page()

    @keyword
    def get_more_video_href(self):
        self.video.get_more_video_content_href()

    @keyword
    def should_be_more_video_page(self):
        self.common.url_should_be_matching('videos')
        self.video.is_more_video_page()
