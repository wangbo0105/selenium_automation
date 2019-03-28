from robot.api.deco import keyword
from pages.comment import Comment
from pages.basepage import BasePage


class CommentLibrary(object):
    def __init__(self):
        self.comment = Comment()
        self.base = BasePage()

    @keyword
    def post_comment(self):
        self.comment.input_comment()
        self.comment.click_submit_btn()

    @keyword
    def check_the_comment_is_successful(self):
        self.comment.check_comment()

    @keyword
    def reply_comment(self):
        self.comment.reply_comment()
        self.comment.click_submit_btn()

    @keyword
    def check_reply_comment(self):
        self.comment.check_reply_comment()

    @keyword
    def give_comment_like(self):
        self.comment.comment_like()

    @keyword
    def check_comment_like_type(self, type):
        self.comment.check_comment_like_type()

