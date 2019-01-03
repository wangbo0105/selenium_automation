from services.BrowserLibrary import BrowserLibrary


class Photopage(BrowserLibrary):
    photo_tab = ('xpath', '//*[@id="app"]/div/div/header/nav[1]/div/ul/li[3]/a')  # 全景图tab
    photo_box_1 = ('class', 'photo-card-single')  # 照片列表作品第一个

    def go_photo_page(self):
        phototab = self.base.findElement(self.photo_tab)
        self.base.click(phototab)
        return self

    def go_photo_detail_page(self):
        photobox_1 = self.base.findElement(self.photo_box_1)
        self.base.click(photobox_1)
        return self

