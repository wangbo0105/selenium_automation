from services.BrowserLibrary import BrowserLibrary


class Blogpage(BrowserLibrary):
    blog_tab = ('xpath', '//*[@id="app"]/div/div/header/nav[1]/div/ul/li[5]/a')  # VEER博客tab

    def go_blog_page(self):
        blogtab = self.base.findElement(self.blog_tab)
        self.base.click(blogtab)
        return self
