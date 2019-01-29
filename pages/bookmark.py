from pages.basepage import BasePage
from pages.personalpage import PersonalPage


class BookMark(BasePage):
    bookmark_btn = ('class', 'btn-watch-later', 0)  # bookmark——button
    bookmark_alert = ('class', 'ant-modal-content', 0)  # bookmark-alert
    bookmark_alert_close_btn = ('class', 'ant-modal-close', 0)  # bookmark-alert-close
    VR_tab = ('class', ' tabs-tab', 3)  # 个人中心-VR书签tab
    content_href_1 = ('class', 'title', 1)  # VR书签tab-第一个作品
    watch_later_icon = ('class', 'operation-buttons', 0)  # 封面bk-icon
    play_overlay = ('class', 'play-overlay', 0)  # bookmark列表内容

    def __init__(self):
        super().__init__()
        self.personal = PersonalPage()
        self.photo_url = None

    def go_bookmark_tab(self):
        self.personal.go_personal_page()
        self.element.click(self.VR_tab)

    def click_bookmark_btn(self):
        self.element.click(self.bookmark_btn)
        self.photo_url = self.window.get_current_url()

    def click_bookmark_alert_close_btn(self):
        self.element.click(self.bookmark_alert_close_btn)

    def click_VR_tab(self):
        self.element.click(self.VR_tab)

    def check_bookmark_in_detail_page(self):
        self.element.is_text_in_element(self.bookmark_btn, '已添加书签')

    def check_bookmark_in_personalpage(self):
        href = self.element.get_attribute_href(self.content_href_1)
        self.element.should_be_equal(self.photo_url, href)

    def clear_bookmark_all(self):
        while self.element.ElementExist(self.play_overlay):
            self.element.click(self.watch_later_icon)
            self.browser.refresh()
