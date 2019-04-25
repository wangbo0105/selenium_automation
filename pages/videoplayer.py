from pages.basepage import BasePage
import time


class VideoPlayer(BasePage):
    play = ('class', 'btn-play', 0)
    pause = ('class', 'btn-pause', 0)

    def click_video_play_btn(self):
        self.element.click(self.play)

    def click_video_pause_btn(self):
        # time.sleep(5)
        self.element.click(self.pause)

    def check_current_state_of_play(self, state):
        if state == 'play':
            self.element.is_element_exist(self.pause)
        elif state == 'pause':
            self.element.is_element_not_exist(self.pause)
        else:
            raise ValueError('传入无效的参数:' + state)
