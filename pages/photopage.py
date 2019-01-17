from pages.basepage import BasePage


class Photopage(BasePage):
    photo_tab = ('class', 'ant-menu-item', 2)  # 导航栏-全景图
    photo_box_1 = ('class', 'photo-card-single', 0)  # 全景图-列表第一个作品
    slogan = ('class', 'slogan', 0)  # 全景图 banner_title
    photo_player = ('class', 'photo-overlay', 0)  # 照片播放器

