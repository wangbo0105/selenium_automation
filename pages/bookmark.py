from pages.basepage import BasePage


class BookMark(object):
    bookmark_btn = ('class', 'btn-watch-later', 0)  # bookmark——button
    bookmark_alert = ('class', 'ant-modal-content', 0)  # bookmark-alert
    bookmark_alert_close_btn = ('class', 'ant-modal-close', 0)  # bookmark-alert-close
    VR_tab = ('class', ' tabs-tab', 3)  # 个人中心-VR书签tab
    content_href_1 = ('class', 'title', 1)  # VR书签tab-第一个作品
    watch_later_icon = ('class', 'operation-buttons', 0)  # 封面bk-icon
    play_overlay = ('class', 'play-overlay', 0)  # bookmark列表内容

    def __init__(self):
        self.base = BasePage()
        self.photo_url = None

    def click_bookmark_btn(self):
        self.base.element.click(self.bookmark_btn)
        self.photo_url = self.base.window.get_current_url()

    def click_bookmark_alert_close_btn(self):
        self.base.element.click(self.bookmark_alert_close_btn)

    def click_VR_tab(self):
        self.base.element.click(self.VR_tab)

    def check_bookmark_in_detail_page(self):
        self.base.element.is_text_in_element(self.bookmark_btn, '已添加书签')

    def check_bookmark_in_personalpage(self):
        href = self.base.element.get_attribute_href(self.content_href_1)
        self.base.element.should_be_equal(self.photo_url, href)

    def clear_bookmark_all(self):
        while self.base.element.ElementExist(self.play_overlay):
            self.base.element.click(self.watch_later_icon)
            self.base.browser.refresh()
