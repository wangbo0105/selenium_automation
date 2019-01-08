from robot.api.deco import keyword
from Base.base import Base


class CommonLibrary(Base):
    url = ('https://stg.veervr.tv/')

    @keyword
    def open_my_browser(self):
        self.open(self.url)

    @keyword
    def refresh_current_page(self):
        self.refresh()

    @keyword
    def close_my_browser(self):
        self.quit()

    @keyword
    def close_current_window(self):
        self.close()

    @keyword
    def goto_page_by_click(self, ele):
        if len(ele) == 2:
            self.click(self.findElement(ele))
        else:
            self.click(self.findElements(ele))

    @keyword
    def goto_page_by_hover(self, ele1, ele2):
        if len(ele1) == 2:
            self.move_to_element(self.findElement(ele1))
            if len(ele2) == 2:
                self.click(self.findElement(ele2))
            else:
                self.click(self.findElements(ele2))
        else:
            if len(ele2) == 2:
                self.click(self.findElement(ele2))
            else:
                self.click(self.findElements(ele2))
