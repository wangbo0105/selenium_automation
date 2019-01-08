from Base.base import Base


class Storepage(Base):
    store_url = ('https://shop525226884.taobao.com/?spm=a230r.7195193.1997079397.2.X5z0kg?utm_source=web-menu')
    store_tab = ('class', 'nav-item', 0)  # 商城tab

    # def go_store_page(self):
    #     self.click(self.findElement(self.store_tab))
    #     return self
