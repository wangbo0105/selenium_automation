from robot.api.deco import keyword
from pages.videopage import VideoPage


class VideoLibrary(object):
    def __init__(self):
        self.video = VideoPage()

    @keyword
    def click_item(self, name):
        self.video.click_item(name)

    @keyword
    def is_video_page(self):
        self.video.match_video_url()
        self.video.is_video_page()

    @keyword
    def is_video_detail_page(self):
        self.video.match_video_url()
        self.video.is_video_detail_page()

    @keyword
    def get_more_video_href(self):
        self.video.get_more_video_content_href()

    @keyword
    def is_more_video_page(self):
        self.video.is_more_video_page()
