from robot.api.deco import keyword
from pages.basepage import BasePage


class CommonLibrary(BasePage):
    url = 'https://stg.veervr.tv/'

    @keyword
    def load_veer(self):
        self.browser.open(self.url)

    @keyword
    def refresh_current_window(self):
        self.browser.refresh()

    @keyword
    def close_my_browser(self):
        self.browser.quit()

    @keyword
    def close_current_window(self):
        self.browser.close()

    @keyword
    def goto_page_by_click(self, ele):
            self.element.click(self.findElements(ele))

    @keyword
    def goto_page_by_hover(self, ele1, ele2):
        self.element.move_to_element(self.findElements(ele1))
        self.element.click(self.findElements(ele2))
