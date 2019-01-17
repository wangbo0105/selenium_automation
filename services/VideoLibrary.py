from robot.api.deco import keyword
from pages.videopage import Videopage
from services.CommonLibrary import CommonLibrary


class VideoLibrary(Videopage):
    cl = CommonLibrary()

    @keyword
    def go_video(self):
        self.cl.goto_page_by_click(self.video_tab)

    @keyword
    def go_video_detail(self):
        self.cl.goto_page_by_click(self.video_box_1)

    @keyword
    def is_video_page(self):
        self.window.is_text_in_url('videos')
        self.element.is_text_in_element(self.slogan, 'VeeR VR 视频')

    @keyword
    def is_video_detail_page(self):
        self.window.is_text_in_url('videos/')
        self.element.is_element_exist(self.video_player)
