from robot.api.deco import keyword
from pages.comment import Comment
from services.PhotoLibrary import PhotoLibrary


class CommentLibrary(Comment):
    pp = PhotoLibrary()

    @keyword
    def post_comment(self, text):
        self.input_comment(text)
        self.click_submit_btn()
        self.is_text_in_element(self.comment_content, text)

