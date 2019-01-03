from services.BrowserLibrary import BrowserLibrary


class Uploadpage(BrowserLibrary):
    upload_tab = ('xpath', '//*[@id="app"]/div/div/header/nav[1]/div/a')  # 上传tab

    def go_upload_page(self):
        uploadtab = self.base.findElement(self.upload_tab)
        self.base.click(uploadtab)
        return self
