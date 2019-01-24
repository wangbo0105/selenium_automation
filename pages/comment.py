from pages.basepage import BasePage


class Comment(BasePage):
    comment_box = ('class', 'ant-input-lg', 0)
    submit_btn = ('class', 'ant-btn', 4)
    comment_content = ('class', 'content', 3)

    def __init__(self):
        super().__init__()
        self.comment_text = None

    def input_comment(self, text):
        self.comment_text = text
        self.element.send_keys(self.comment_box, text)

    def click_submit_btn(self):
        self.element.click(self.submit_btn)

    def check_comment(self):
        self.element.is_text_in_element(self.comment_content, self.comment_text)
