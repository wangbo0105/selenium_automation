from pages.basepage import BasePage
from pages.personalpage import PersonalPage


class BookMark(BasePage):
    bookmark_btn = ('class', 'btn-watch-later', 0)  # bookmark——button
    bookmark_helper_btn = ('class', 'btn-watch-later', 1)  # bookmark_帮助button
    bookmark_helper_alert = ('class', 'watch-later-in-vr--content', 0)  # bookmark_帮助弹窗
    bookmark_alert = ('class', 'ant-modal-content', 0)  # bookmark-alert
    bookmark_alert_close_btn = ('class', 'ant-modal-close', 0)  # bookmark-alert-close
    content_href = ('xpath', '//div[@class="play-overlay"]/a', 0)  # VR书签tab-第一个作品
    bookmark_icon = ('class', 'watch-later-in-vr', 0)  # 封面bk-icon
    play_overlay = ('class', 'play-overlay', 0)  # bookmark列表内容
    bookmarks_type = ('class', 'bookmarks-type', 0)  # VR书签tab 筛选框

    def __init__(self):
        super().__init__()
        self.personal = PersonalPage()
        self.content_url = None

    def click_bookmark_btn(self):
        self.element.click(self.bookmark_btn)
        self.content_url = self.window.get_current_url()

    def click_bookmark_helper_btn(self):
        self.element.click(self.bookmark_helper_btn)

    def check_bookmark_helper_alert(self):
        att = self.element.get_attribute(self.bookmark_helper_alert, 'style')
        self.element.should_contains(att, 'block')

    def click_bookmark_alert_close_btn(self):
        alert = self.element.ElementExist(self.bookmark_alert)
        if alert:
            self.element.click(self.bookmark_alert_close_btn)

    def check_bookmark_in_detail_page(self):
        self.element.is_text_in_element(self.bookmark_btn, '已添加书签')

    def click_bookmark_icon(self):
        self.element.click(self.bookmark_icon)
        self.content_url = self.element.get_attribute_href(self.content_href)

    def check_bookmark_in_surface(self):
        _active = self.element.get_attribute(self.bookmark_icon, 'class')
        self.element.should_contains(_active, 'active')

    def check_bookmark_in_personalpage(self):
        href = self.element.get_attribute_href(self.content_href)
        self.element.should_be_equal(self.content_url, href)

    def remove_bookmark_in_detail(self):
        self.element.click(self.bookmark_btn)

    def check_remove_bookmark_in_detail(self):
        self.element.is_text_in_element(self.bookmark_btn, '加入VR书签')

    def check_remove_bookmark_in_personal(self):
        self.element.is_element_not_exist(self.play_overlay)

    @staticmethod
    def bookmark_type_dict(name):
        item_name = {'所有书签': ('xpath', '//li/a[text()=\"%s\"]' % name, 0),
                     '照片': ('xpath', '//li/a[text()=\"%s\"]' % name, 0),
                     '视频': ('xpath', '//li/a[text()=\"%s\"]' % name, 2),
                     '互动体验': ('xpath', '//li/a[text()=\"%s\"]' % name, 2),
                     }
        return item_name[name]

    def get_bookmark_type(self, name):
        item = self.bookmark_type_dict(name)
        return item

    def switch_screen_type(self, name):
        self.element.click(self.bookmarks_type)
        self.element.click(self.get_bookmark_type(name))

    def check_screen_results(self, name):
        self.element.is_text_in_element(self.bookmarks_type, name)

    def clear_bookmark_all(self):
        while self.element.ElementExist(self.play_overlay):
            self.element.click(self.bookmark_icon)
            self.browser.refresh()
        self.element.is_element_not_exist(self.play_overlay)
