from robot.api.deco import keyword
from pages.blogpage import BlogPage
from pages.storepage import StorePage


class ExternalLibrary(object):
    def __init__(self):
        self.blog = BlogPage()
        self.store = StorePage()

    @keyword
    def should_be_blog_page(self):
        self.blog.is_blog_page()

    @keyword
    def should_be_store_page(self):
        self.store.is_store_page()
