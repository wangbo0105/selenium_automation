from pages.basepage import BasePage


class Videopage(BasePage):
    video_tab = ('class', 'ant-menu-item', 1)  # 导航栏-视频
    video_box_1 = ('class', 'play-overlay', 0)  # 精选视频，第一个作品
    video_tabs_tab = ('class', 'tabs-tab', 0)  # 精选视频-tab
    slogan = ('class', 'slogan', 0)  # 精选视频banner-标题
    video_player = ('class', 'video-player', 0)  # 精选视频播放详情页-video_player
