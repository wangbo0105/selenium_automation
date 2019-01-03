from robot.api.deco import keyword
from pages.videopage import Videopage


class VideoLibrary(Videopage):
    @keyword
    def go_video(self):
        self.go_video_page()

    @keyword
    def go_video_detail(self):
        self.go_video_detail_page()
