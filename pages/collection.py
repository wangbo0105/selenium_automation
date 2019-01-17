from pages.basepage import BasePage


class Collection(BasePage):
    add_collection_btn = ('class', 'content-add-to-collection', 0)
    add_collection_box = ('class', 'collection-title', 0)
    smoke_collection = ('link_text', 'smoke', 0)
    contained = ('class', 'contained', 0)
    collection_tab = ('class', ' tabs-tab', 2)  # 个人中心-collection tab
    create_collection_btn = ('class', 'collection-create-btn', 0)  # 创建合辑btn
    create_title_input_box = ('class', 'ant-input-lg', 0)  # 创建合辑-title输入框
    create_safe_btn = ('class', 'save-btn', 0)  # 创建合辑-保存button
    collection_box_1 = ('class', 'title', 1)  # collection tab -第一个合辑
    content_href_1 = ('class', 'title', 3)  # collection box-第一个作品

    def click_add_collection_btn(self):
        self.click(self.findElements(self.add_collection_btn))

    def add_collection(self):
        self.click(self.findElements(self.add_collection_box))

    def click_collection_tab(self):
        self.click(self.findElements(self.collection_tab))

    def click_collection_box_1(self):
        self.click(self.findElements(self.collection_box_1))

    def get_content_href_1(self):
        return self.get_attribute(self.findElements(self.content_href_1), 'href')

    def click_create_collection(self):
        self.click(self.findElements(self.create_collection_btn))

    def input_cc_title(self, title):
        self.send_keys(self.findElements(self.create_title_input_box), title)

    def click_cc_safe_btn(self):
        self.click(self.findElements(self.create_safe_btn))

    def get_collection_box_href_1(self):
        return self.get_attribute(self.findElements(self.collection_box_1), 'href')


