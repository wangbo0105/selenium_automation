from robot.api.deco import keyword
from pages.videoplayer import VideoPlayer
from pages.videopage import VideoPage
from services.CommonLibrary import CommonLibrary
import time


class VideoPlayerLibrary(object):
    def __init__(self):
        self.video = VideoPage()
        self.video_player = VideoPlayer()
        self.common = CommonLibrary()

    @keyword()
    def go_video_player(self):
        self.common.go_page('video')
        self.video.click_item('video_content')
        time.sleep(2)

    @keyword()
    def play_video(self):
        self.video_player.click_video_play_btn()

    @keyword()
    def pause_video(self):
        self.video_player.click_video_pause_btn()

    @keyword()
    def check_video_state(self, state):
        self.video_player.check_current_state_of_play(state)

    @keyword()
    def switch_resolution(self, reso):
        time.sleep(2)
        self.video_player.switching_resolution(reso)

    @keyword()
    def check_current_resolution(self, reso):
        self.video_player.check_current_resolution(reso)

    @keyword()
    def switch_fullscreen(self):
        self.video_player.switch_fullscreen()

    @keyword()
    def check_fullscreen_state(self, fullscreen):
        self.video_player.check_fullscreen(fullscreen)