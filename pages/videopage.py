from pages.basepage import BasePage


class Videopage(BasePage):
    video_tab = ('class', 'ant-menu-item', 1)  # 视频tab
    video_box_1 = ('class', 'play-overlay')  # 视频列表作品第一个
    video_tabs_tab = ('class', 'tabs-tab', 0)  # 精选视频tab
    slogan = ('class', 'slogan')  # 视频页banner标题
    video_player = ('class', 'video-player')  # video-player
