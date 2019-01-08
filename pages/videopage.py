from Base.base import Base


class Videopage(Base):
    video_tab = ('class', 'ant-menu-item', 1)  # 视频tab
    video_box_1 = ('class', 'video-info-box')  # 视频列表作品第一个
    video_tabs_tab = ('class', 'tabs-tab', 0)  # 精选视频tab
    slogan = ('class', 'slogan')  # 视频页banner标题
    video_player = ('class', 'video-player')  # video-player

    # def go_video_page(self):
    #     videotab = self.findElement(self.video_tab)
    #     self.click(videotab)
    #     return self
    #
    # def go_video_detail_page(self):
    #     videobox_1 = self.findElement(self.video_box_1)
    #     self.click(videobox_1)
    #     return self
    #
    # def is_video(self):
    #     self.is_text_in_url('video')


# if __name__ == '__main__':
#     Videopage().open('http://stg.veervr.tv')
#     Videopage().go_video_page()
