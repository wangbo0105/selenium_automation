from pages.basepage import BasePage


class PhotoPage(BasePage):
    photo_player = ('class', 'photo-player', 0)
    more_photo = ('css', '.image-responsive img', 0)
    content_name = ('xpath', '//div[@class="title-delta"]/h1', 0)

    tabs_tab_active = 'tabs-tab-active'
    photo_name_text = None

    @staticmethod
    def photo_page_dict():
        item_name = {'featured': ('class', 'tabs-tab', 0),
                     'popular': ('class', 'tabs-tab', 1),
                     'recent': ('class', 'tabs-tab', 2),
                     'photo_content': ('css', 'div.photo-overlay > img', 0), }
        return item_name

    def click_item(self, name):
        item = self.photo_page_dict()
        self.js.js_scroll(0, 100)
        # self.window.get_error_screenshot()
        self.element.click(item[name])
        # self.window.get_error_screenshot()

    def is_photo_detail_page(self):
        self.element.is_element_exist(self.photo_player)

    def get_current_content_name(self):
        return self.element.get_text(self.content_name)

    def is_selected_tab(self, name):
        self.window.is_text_in_url(name)
        item = self.photo_page_dict()
        active = self.element.get_attribute(item[name], 'class')
        self.element.should_contains(active, self.tabs_tab_active)

    def click_more_photo(self):
        self.photo_name_text = self.element.get_attribute(self.more_photo, 'alt')
        self.element.click(self.more_photo)

    def is_more_photo_page(self):
        _text = self.element.get_text(self.content_name)
        self.element.should_be_equal(self.photo_name_text, _text)
        self.photo_name_text = None
