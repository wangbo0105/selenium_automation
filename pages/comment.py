from pages.basepage import BasePage
from module.random_generator import RandomGenerator
import time


class Comment(BasePage):
    comment_box = ('class', 'ant-input-lg', 0)
    submit_btn = ('class', 'ant-btn', 4)
    comment_content = ('xpath', '//div[@class="comment-box"]/div/div[2]', 0)
    comment_user_name = ('xpath', '//div[@class="comment-box"]/div/div/div/a', 0)
    comment_like_btn = ('xpath', '//div[@class="comment-box"]/div/div/div[2]', 0)
    comment_liked_btn = ('class', 'liked', 0)
    reply = ('class', 'reply', 0)

    def __init__(self):
        super().__init__()
        self.random = RandomGenerator()
        self._comment_user = None
        self.comment_text = None

    def input_comment(self):
        self.comment_text = self.random.random_comments()
        self.element.send_keys(self.comment_box, self.comment_text)

    def reply_comment(self):
        self.js.js_scroll(0, 500)
        self.comment_text = self.random.random_comments(5)
        self._comment_user = self.element.get_text(self.comment_user_name)
        self.element.click(self.reply)
        self.element.send_keys(self.comment_box, self.comment_text)

    def click_submit_btn(self):
        self.element.click(self.submit_btn)
        time.sleep(2)

    def check_comment(self):
        self.element.is_text_in_element(self.comment_content, self.comment_text)

    def check_reply_comment(self):
        _comment_text = ('@' + self._comment_user + ' ' + self.comment_text)
        _value = self.element.get_text(self.comment_content)
        self.element.should_be_equal(_value, _comment_text)

    def comment_like(self):
        self.js.js_scroll(0, 500)
        self.element.click(self.comment_like_btn)

    def check_comment_like_type(self, type=True):
        value = self.element.get_attribute(self.comment_like_btn, 'class')
        if type:
            self.element.should_contains(value, 'liked')
        else:
            self.element.should_not_contains(value, 'liked')
