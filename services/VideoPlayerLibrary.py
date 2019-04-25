from robot.api.deco import keyword
from pages.videoplayer import VideoPlayer
from pages.videopage import VideoPage
from services.CommonLibrary import CommonLibrary


class VideoPlayerLibrary(object):
    def __init__(self):
        self.video = VideoPage()
        self.video_player = VideoPlayer()
        self.common = CommonLibrary()

    @keyword()
    def go_video_player(self):
        self.common.go_page('video')
        self.video.click_item('video_content')

    @keyword()
    def play_video(self):
        self.video_player.click_video_play_btn()

    @keyword()
    def pause_video(self):
        self.video_player.click_video_pause_btn()

    @keyword()
    def check_video_state(self, state):
        self.video_player.check_current_state_of_play(state)
