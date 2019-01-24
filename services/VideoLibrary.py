from robot.api.deco import keyword
from pages.videopage import Videopage


class VideoLibrary(object):
    def __init__(self):
        self.video = Videopage()

    @keyword
    def go_video_detail(self):
        self.video.get_video_content_href()
        self.video.click_video_content_1()

    @keyword
    def is_video_page(self):
        self.video.is_video_page()

    @keyword
    def is_video_detail_page(self):
        self.video.is_video_detail_page()

    @keyword
    def click_more_video_content(self):
        self.video.get_more_video_content_href()
        self.video.click_more_video()

    @keyword
    def is_more_video_page(self):
        self.video.is_more_video_page()
