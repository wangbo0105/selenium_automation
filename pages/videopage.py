from services.BrowserLibrary import BrowserLibrary


class Videopage(BrowserLibrary):
    video_tab = ('xpath', '//*[@id="app"]/div/div/header/nav[1]/div/ul/li[2]/a')  # 视频tab
    video_box_1 = ('class', 'video-info-box')  # 视频列表作品第一个

    def go_video_page(self):
        videotab = self.base.findElement(self.video_tab)
        self.base.click(videotab)
        return self

    def go_video_detail_page(self):
        videobox_1 = self.base.findElement(self.video_box_1)
        self.base.click(videobox_1)
        return self
