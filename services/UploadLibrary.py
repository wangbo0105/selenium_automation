from robot.api.deco import keyword
from pages.uploadpage import Uploadpage


class UploadLibrary(Uploadpage):
    @keyword
    def go_upload(self):
        self.go_upload_page()
