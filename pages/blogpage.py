from pages.basepage import BasePage


class Blogpage(object):
    blog_tab = ('class', 'ant-menu-item', 4)  # 导航栏-VEER博客
    navbar_brand = ('class', 'navbar-brand', 0)  # 博客-header-VeeR VR 博客

    def __init__(self):
        self.base = BasePage()

    def is_blog_page(self):
        self.base.window.switch_handle()
        self.base.window.is_text_in_url('blog')
        self.base.element.is_element_exist(self.navbar_brand)
