from pages.basepage import BasePage


class BlogPage(BasePage):
    blog_tab = ('class', 'ant-menu-item', 4)  # 导航栏-VEER博客
    navbar_brand = ('class', 'navbar-brand', 0)  # 博客-header-VeeR VR 博客

    def is_blog_page(self):
        self.window.switch_handle()
        self.window.is_text_in_url('blog')
        self.element.is_element_exist(self.navbar_brand)
