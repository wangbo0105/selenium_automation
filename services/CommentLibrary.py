from robot.api.deco import keyword
from pages.comment import Comment
from pages.basepage import BasePage


class CommentLibrary(object):
    def __init__(self):
        self.comment = Comment()
        self.base = BasePage()

    @keyword
    def post_comment(self, text):
        self.comment.input_comment(text)
        self.comment.click_submit_btn()

    @keyword
    def check_comment(self):
        self.comment.check_comment()

