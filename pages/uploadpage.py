from pages.basepage import BasePage


class Uploadpage(object):
    upload_tab = ('class', 'upload-btn', 0)  # 导航栏-上传
    upload_title = ('class', 'upload-title', 0)  # 上传页面-标题

    def __init__(self):
        self.base = BasePage()

    def is_upload_page(self):
        self.base.window.is_text_in_url('upload')
        self.base.element.is_element_exist(self.upload_title)
