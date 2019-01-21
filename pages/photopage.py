from pages.basepage import BasePage


class Photopage(object):
    photo_tab = ('class', 'ant-menu-item', 2)  # 导航栏-全景图
    photo_content_1 = ('class', 'photo-card-single', 0)  # 全景图-列表第一个作品
    slogan = ('class', 'slogan', 0)  # 全景图 banner_title
    slogan_name = 'VeeR 360 全景图'
    photo_player = ('class', 'photo-overlay', 0)  # 照片播放器

    def __init__(self):
        self.base = BasePage()

    def click_photo_content_1(self):
        self.base.element.click(self.photo_content_1)

    def is_photo_page(self):
        self.base.window.is_text_in_url('photo')
        self.base.element.is_text_in_element(self.slogan, self.slogan_name)

    def is_photo_detail_page(self):
        self.base.window.is_text_in_url('photos/')
        self.base.element.is_element_exist(self.photo_player)
