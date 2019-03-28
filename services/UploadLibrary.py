from robot.api.deco import keyword
from pages.uploadpage import UploadPage


class UploadLibrary(object):
    def __init__(self):
        self.upload = UploadPage()

    @keyword
    def select_upload(self):
        self.upload.click_upload()
        self.upload.is_upload_page()

    @keyword
    def should_be_upload_page(self):
        self.upload.is_upload_page()

    @keyword
    def upload_one_photo(self):
        self.upload.upload_one_photo()

    @keyword
    def is_upload_page(self):
        self.upload.is_photo_Upload_page()
        
