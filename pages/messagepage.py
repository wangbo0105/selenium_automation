from services.BrowserLibrary import BrowserLibrary


class Messagepage(BrowserLibrary):
    message_box = ('class', 'message-box-header')  # 消息盒子

    def go_message_page(self):
        messagebox = self.base.findElement(self.message_box)
        self.base.click(messagebox)
        return self
