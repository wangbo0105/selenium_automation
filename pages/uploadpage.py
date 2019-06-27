from pages.basepage import BasePage
import time


class UploadPage(BasePage):
    upload_tab = ('class', 'upload-btn', 0)  # 导航栏-上传
    upload_title = ('class', 'upload-title', 0)  # 上传页面-标题
    # uoplodBtn = ('xpath','//input[@id="fileSelector"]',0)
    uoplodBtn = ('id', 'fileSelector', 0)

    photoCanvas = ('class', 'photo-preview', 0)

    def click_upload(self):
        self.element.click(self.upload_tab)

    def is_upload_page(self):
        self.window.is_text_in_url('upload')
        self.element.is_element_exist(self.upload_title)

    def upload_one_photo(self):
        self.element.send_keys(self.uoplodBtn, "/Users/cc/testfile/test_photos/ gear/gear_road/IMG_0647.JPG")

    def is_photo_Upload_page(self):
        time.sleep(4)
        self.element.is_element_exist(self.photoCanvas)
