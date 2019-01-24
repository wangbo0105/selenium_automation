from robot.api.deco import keyword
from pages.blogpage import BlogPage


class BlogLibrary(object):
    def __init__(self):
        self.bl = BlogPage()

    @keyword
    def is_blog_page(self):
        self.bl.is_blog_page()
