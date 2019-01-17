from pages.basepage import BasePage


class BookMark(BasePage):
    bookmark_btn = ('class', 'btn-watch-later', 0)  # bookmark——button
    bookmark_alert = ('class', 'ant-modal-content', 0)  # bookmark-alert
    bookmark_alert_close_btn = ('class', 'ant-modal-close', 0)  # bookmark-alert-close
    VR_tab = ('class', ' tabs-tab', 3)  # 个人中心-VR书签tab
    content_href_1 = ('class', 'title', 1)  # like tab-第一个作品
    watch_later_icon = ('class', 'operation-buttons', 0)  # 封面bk-icon
    play_overlay = ('class', 'play-overlay', 0)  # bookmark列表内容

    def click_bookmark_btn(self):
        self.click(self.findElements(self.bookmark_btn))

    def click_bookmark_alert_close_btn(self):
        self.click(self.findElements(self.bookmark_alert_close_btn))

    def click_VR_tab(self):
        self.click(self.findElements(self.VR_tab))

    def get_content_href_1(self):
        return self.get_attribute(self.findElements(self.content_href_1), 'href')

    def clear_bookmark_all(self):
        while self.ElementExist(self.play_overlay):
            self.click(self.findElements(self.watch_later_icon))
            self.refresh()
