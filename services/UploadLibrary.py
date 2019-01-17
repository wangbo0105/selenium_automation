from robot.api.deco import keyword
from pages.uploadpage import Uploadpage
from services.CommonLibrary import CommonLibrary


class UploadLibrary(Uploadpage):
    cl = CommonLibrary()

    @keyword
    def go_upload(self):
        self.cl.goto_page_by_click(self.upload_tab)

    @keyword
    def is_upload_page(self):
        self.is_text_in_url('upload')
        self.is_element_exist(self.upload_title)
