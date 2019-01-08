from Base.base import Base


class Photopage(Base):
    photo_tab = ('class', 'ant-menu-item', 2)  # 全景图tab
    photo_box_1 = ('class', 'photo-card-single')  # 照片列表作品第一个
    slogan = ('class', 'slogan')  # 全景图主页slogan
    photo_player = ('class', 'photo-player')  # 照片播放器

    # def go_photo_page(self):
    #     self.click(self.findElement(self.photo_tab))
    #     return self
    #
    # def go_photo_detail_page(self):
    #     self.click(self.findElement(self.photo_box_1))
    #     return self

