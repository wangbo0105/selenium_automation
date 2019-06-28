from pages.basepage import BasePage
import time


class VideoPlayer(BasePage):
    play = ('class', 'btn-play', 0)
    pause = ('class', 'btn-pause', 0)
    resolution_btn = ('class', 'video-resolution', 0)
    current_resolution = ('class', 'js-current-resolution', 0)
    fullscreen_btn = ('class', 'fullscreen-toggle', 0)

    @staticmethod
    def reso_dict():
        item_name = {'2160p': ('class', 'reso-2160', 0),
                     '1440p': ('class', 'reso-1440', 0),
                     '1080p': ('class', 'reso-1080', 0),
                     '720p': ('class', 'reso-720', 0)
                     }
        return item_name

    def click_video_play_btn(self):
        self.element.click(self.play)

    def click_video_pause_btn(self):
        # time.sleep(5)
        self.element.click(self.pause)

    def check_current_state_of_play(self, state):
        if state == 'play':
            time.sleep(5)  # 避免网络不好时资源加载慢，造成错误判断影响
            self.element.is_element_exist(self.pause)
        elif state == 'pause':
            self.element.is_element_not_exist(self.pause)
        else:
            raise ValueError('传入无效的参数:' + state)

    def switching_resolution(self, reso):
        _reso = VideoPlayer().reso_dict()
        self.element.click(self.resolution_btn)
        self.element.click(_reso[reso])

    def check_current_resolution(self, reso):
        _reso = self.reso_dict()
        _selected = self.element.get_attribute(_reso[reso], 'class')
        self.element.should_contains(_selected, 'selected')
        self.element.is_text_in_element(self.current_resolution, reso)

    def switch_fullscreen(self):
        self.element.click(self.fullscreen_btn)

    def check_fullscreen(self, fullscreen=True):
        _full = self.element.get_attribute(self.fullscreen_btn, 'class')
        if fullscreen:
            self.element.should_contains(_full, 'shrink')
        else:
            self.element.should_not_contains(_full, 'shrink')
