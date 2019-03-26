from pages.basepage import BasePage
import time


class Like(BasePage):
    like_button = ('class', 'like-button', 0)
    liked_button = ('class', 'liked', 0)
    play_overlay = ('class', 'play-overlay', 0)

    def __init__(self):
        super().__init__()
        self.content_href = None

    def click_like_button(self):
        self.content_href = self.window.get_current_url()
        self.element.click(self.like_button)

    def click_unlike_button(self):
        self.element.click(self.liked_button)

    def check_liked_in_detail_page(self):
        self.element.is_element_exist(self.liked_button)

    def check_unlike_in_detail_page(self):
        self.element.is_element_not_exist(self.liked_button)

    @staticmethod
    def liked_type_dict():
        item_name = {'liked_photo': ('xpath', "//div[contains(text(),'喜欢的照片')]", 0),
                     'liked_video': ('xpath', "//div[contains(text(),'喜欢的视频')]", 0),
                     'liked_experience': ('xpath', "//div[contains(text(),'喜欢的互动体验')]", 0),
                     'liked_collection': ('xpath', "//div[contains(text(),'喜欢的合辑')]", 0)
                     }
        return item_name

    def get_liked_type(self, name):
        item = self.liked_type_dict()
        return item[name]

    @staticmethod
    def liked_content_dict():
        item_name = {'liked_photo': ('xpath', "//div[contains(text(),'喜欢的照片')]/../../div[2]/div/div/div[2]/div/a", 0),
                     'liked_video': ('xpath', "//div[contains(text(),'喜欢的视频')]/../../div[2]/div/div/div[2]/div/a", 0),
                     'liked_experience': (
                         'xpath', "//div[contains(text(),'喜欢的互动体验')]/../../div[2]/div/div/div[2]/div/a", 0),
                     'liked_collection': (
                         'xpath', "//div[contains(text(),'喜欢的合辑')]/../../div[2]/div/div/div[2]/div/a", 0),

                     }
        return item_name

    def get_liked_content(self, name):
        item = self.liked_content_dict()
        return item[name]

    def check_liked_type_exited(self, name):
        self.element.is_element_exist(self.get_liked_type(name))

    def check_liked_content_exited(self, name):
        self.element.should_contains(self.content_href, self.element.get_attribute_href(self.get_liked_content(name)))

    def check_liked_content_removed(self, name):
        self.element.is_element_not_exist(self.get_liked_type(name))
        self.element.is_element_not_exist(self.get_liked_content(name))

    def click_liked_tab_content(self, name):
        self.element.click(self.get_liked_content(name))

    def clear_like_all(self):
        while self.element.ElementExist(self.play_overlay):
            self.element.click(self.play_overlay)
            self.element.click(self.liked_button)
            self.browser.back()
            time.sleep(2)
        self.element.is_element_not_exist(self.play_overlay)
