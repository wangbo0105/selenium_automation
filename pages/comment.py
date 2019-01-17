from pages.basepage import BasePage


class Comment(BasePage):
    comment_box = ('class', 'ant-input-lg', 0)
    submit_btn = ('class', 'ant-btn', 4)
    comment_content = ('class', 'content', 3)

    def input_comment(self, text):
        self.send_keys(self.findElements(self.comment_box), text)

    def click_submit_btn(self):
        self.click(self.findElements(self.submit_btn))
