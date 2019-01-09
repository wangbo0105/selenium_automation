from robot.api.deco import keyword
from pages.basepage import BasePage


class CommonLibrary(BasePage):
    url = ('https://stg.veervr.tv/')

    @keyword
    def open_my_browser(self):
        self.browser.open(self.url)

    @keyword
    def refresh_current_page(self):
        self.browser.refresh()

    @keyword
    def close_my_browser(self):
        self.browser.quit()

    @keyword
    def close_current_window(self):
        self.browser.close()

    @keyword
    def goto_page_by_click(self, ele):
        if len(ele) == 2:
            self.element.click(self.findElement(ele))
        else:
            self.element.click(self.findElements(ele))

    @keyword
    def goto_page_by_hover(self, ele1, ele2):
        if len(ele1) == 2:
            self.element.move_to_element(self.findElement(ele1))
            if len(ele2) == 2:
                self.element.click(self.findElement(ele2))
            else:
                self.element.click(self.findElements(ele2))
        else:
            if len(ele2) == 2:
                self.element.click(self.findElement(ele2))
            else:
                self.element.click(self.findElements(ele2))
