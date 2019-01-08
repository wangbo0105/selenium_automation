from Base.base import Base


class Messagepage(Base):
    message_box = ('class', 'message-box-header')  # 消息盒子
    page_bar_title = ('class', 'inner-page-title')  # 消息盒子页面-消息标识

    # def go_message_page(self):
    #     self.click(self.findElement(self.message_box))
    #     return self
