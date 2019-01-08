from Base.base import Base


class Exppage(Base):
    exp_tab = ('class', 'ant-menu-item', 3)  # 互动体验 tab
    learn_more_1 = ('class', 'ant-btn-primary-ghost', 1)  # 了解更多第一个
    load_layer = ('class', 'load-layer')  # exp播放器

    # def go_exp_page(self):
    #     self.click(self.findElement(self.exp_tab))
    #     return self
    #
    # def go_exp_detail_page(self):
    #     self.click(self.findElement(self.learn_more_1))
    #     return self

