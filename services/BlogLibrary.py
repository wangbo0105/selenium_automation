from robot.api.deco import keyword
from pages.blogpage import Blogpage
from services.CommonLibrary import CommonLibrary


class BlogLibrary(Blogpage):
    cl = CommonLibrary()

    @keyword
    def go_blog(self):
        # self.go_blog_page()
        self.cl.goto_page_by_click(self.blog_tab)

    @keyword
    def is_blog_page(self):
        self.switch_handle()
        self.is_text_in_url('blog')
        self.isElementExist(self.navbar_brand)
