from Base.base import Base


class Uploadpage(Base):
    upload_tab = ('class', 'upload-btn')  # 上传tab
    upload_title = ('class', 'upload-title')  # upload title

    # def go_upload_page(self):
    #     self.click(self.findElement(self.upload_tab))
    #     return self
