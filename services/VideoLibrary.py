from robot.api.deco import keyword
from pages.videopage import VideoPage


class VideoLibrary(object):
    def __init__(self):
        self.video = VideoPage()

    @keyword
    def video_click_item(self, name):
        self.video.click_item(name)

    @keyword
    def should_be_video_page(self):
        self.video.match_video_url()
        self.video.is_video_page()

    @keyword
    def should_be_video_detail_page(self):
        self.video.match_video_url()
        self.video.is_video_detail_page()

    @keyword
    def should_be_more_video_page(self):
        self.video.match_video_url()
        self.video.is_video_detail_page()
