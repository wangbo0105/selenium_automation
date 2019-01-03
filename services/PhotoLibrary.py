from robot.api.deco import keyword
from pages.photopage import Photopage


class PhotoLibrary(Photopage):
    @keyword
    def go_video(self):
        self.go_photo_page()

    @keyword
    def go_video_detail(self):
        self.go_photo_detail_page()
