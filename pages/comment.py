from pages.basepage import BasePage
from module.random_generator import RandomGenerator


class Comment(BasePage):
    comment_box = ('class', 'ant-input-lg', 0)
    submit_btn = ('class', 'ant-btn', 4)
    comment_content = ('xpath', '//div[@class="comment-box"]/div/div[2]', 0)

    def __init__(self):
        super().__init__()
        self.random = RandomGenerator()
        self.comment_text = None

    def input_comment(self):
        self.comment_text = self.random.random_comments()
        self.element.send_keys(self.comment_box, self.comment_text)

    def click_submit_btn(self):
        self.element.click(self.submit_btn)

    def check_comment(self):
        self.element.is_text_in_element(self.comment_content, self.comment_text)
