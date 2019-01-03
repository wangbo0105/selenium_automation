from robot.api.deco import keyword
from pages.blogpage import Blogpage


class BlogLibrary(Blogpage):
    @keyword
    def go_blog(self):
        self.go_blog_page()
