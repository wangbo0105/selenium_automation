from robot.api.deco import keyword
from pages.uploadpage import Uploadpage


class UploadLibrary(object):
    def __init__(self):
        self.upload = Uploadpage()

    @keyword
    def is_upload_page(self):
        self.upload.is_upload_page()
