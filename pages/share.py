from pages.basepage import BasePage
from pages.comment import Comment
import time

class Share(BasePage):
    share_btn = ('xpath', "//div[contains(text(),'分享')]", 0)
    ant_modal_content = ('class', 'ant-modal-body', 0)
    close_x = ('class', 'ant-modal-close-x', 0)
    pagePath = ('id', 'pagePath', 0)
    embedPath = ('id', 'embedPath', 0)

    def __init__(self):
        super().__init__()
        self.comment = Comment()
        self._link = None
        self.handle = None

    def click_share_btn(self):
        self.js.js_scroll(0, 500)
        self.element.click(self.share_btn)

    @staticmethod
    def channels_dict():
        item_name = {'wechat': ('xpath', '//div[@class="channels"]/div', 0),
                     'moment': ('xpath', '//div[@class="channels"]/div[2]', 0),
                     'weibo': ('xpath', '//div[@class="channels"]/div[3]', 0),
                     'qq': ('xpath', '//div[@class="channels"]/div[4]', 0),
                     'qq_zone': ('xpath', '//div[@class="channels"]/div[5]', 0),
                     'content_link': ('class', 'page-copy-btn', 0),
                     'html_embed_link': ('class', 'embed-copy-btn', 0)}
        return item_name

    @staticmethod
    def channels_item_dict():
        item_name = {'wechat': ('xpath', '//div[contains(text(),"分享到微信")]', 0),
                     'moment': ('xpath', '//div[contains(text(),"分享到微信")]', 0),
                     }
        return item_name

    def click_channels_item(self, name):
        self.handle = self.window.get_current_handle()
        item = Share().channels_dict()
        self.element.click(item[name])

    def check_channels_results(self, name):
        item = Share().channels_item_dict()
        if name == 'weibo':
            self.window.switch_handle()
            url = self.window.get_current_url()
            self.element.should_contains(url, 'service.weibo.com/share')
            self.window.close()
            self.window.switch_handles(self.handle)
        elif name == 'qq':
            self.window.switch_handle()
            url = self.window.get_current_url()
            self.element.should_contains(url, 'shareqq')
            self.window.close()
            self.window.switch_handles(self.handle)
        elif name == 'qq_zone':
            self.window.switch_handle()
            url = self.window.get_current_url()
            self.element.should_contains(url, 'qzshare')
            self.window.close()
            self.window.switch_handles(self.handle)
        elif name == 'wechat' or 'moment':
            self.element.click(self.ant_modal_content)
            self.element.is_element_exist(item[name])
            self.element.click(self.close_x)

    def check_share_link(self, name):
        if name == 'content_link':
            self._link = self.element.get_attribute(self.pagePath, 'value')
        elif name == 'html_embed_link':
            self._link = self.element.get_attribute(self.embedPath, 'value')
        self.element.click(self.share_btn)
        self.element.paste(self.comment.comment_box)
        _text = self.element.get_text(self.comment.comment_box)
        self.element.should_be_equal(self._link, _text)
