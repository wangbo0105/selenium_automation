from pages.basepage import BasePage


class Videopage(object):
    video_tab = ('class', 'ant-menu-item', 1)  # 导航栏-视频
    video_box_1 = ('class', 'play-overlay', 0)  # 精选视频，第一个作品
    video_tabs_tab = ('class', 'tabs-tab', 0)  # 精选视频-tab
    slogan = ('class', 'slogan', 0)  # 精选视频banner-标题
    slogan_name = 'VeeR VR 视频'
    video_player = ('class', 'video-player', 0)  # 精选视频播放详情页-video_player

    def __init__(self):
        self.base = BasePage()

    def click_video_content_1(self):
        self.base.element.click(self.video_box_1)

    def is_video_page(self):
        self.base.window.is_text_in_url('videos')
        self.base.element.is_text_in_element(self.slogan, self.slogan_name)

    def is_video_detail_page(self):
        self.base.window.is_text_in_url('videos/')
        self.base.element.is_element_exist(self.video_player)
