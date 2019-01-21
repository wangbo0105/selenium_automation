from pages.basepage import BasePage


class Collection(object):
    add_collection_btn = ('class', 'content-add-to-collection', 0)
    add_collection_box = ('class', 'collection-title', 0)
    smoke_collection = ('link_text', 'smoke', 0)
    contained = ('class', 'contained', 0)
    collection_tab = ('class', ' tabs-tab', 2)  # 个人中心-collection tab
    create_collection_btn = ('class', 'collection-create-btn', 0)  # 创建合辑btn
    create_title_input_box = ('class', 'ant-input-lg', 0)  # 创建合辑-title输入框
    create_safe_btn = ('class', 'save-btn', 0)  # 创建合辑-保存button
    collection_create_box = ('class', 'collection-create-box', 0)  # collection-create-box
    collection_box_del_btn = ('class', 'delete', 0)  # collection 删除button
    collection_box_del_yes = ('class', 'ant-btn-ghost', 2)  # collection 删除-确认删除
    collection_box_del_no = ('class', 'ant-btn-primary-ghost', 2)  # collection 删除-取消删除
    collection_box_1 = ('class', 'title', 1)  # collection tab -第一个合辑
    content_href_1 = ('class', 'title', 3)  # collection box-第一个作品

    def __init__(self):
        self.base = BasePage()
        self.photo_url = None

    def click_add_collection_btn(self):
        self.photo_url = self.base.window.get_current_url()
        self.base.element.click(self.add_collection_btn)

    def add_collection(self):
        self.base.element.click(self.add_collection_box)

    def check_collection_in_detail_page(self):
        self.base.element.is_element_exist(self.contained)

    def click_collection_tab(self):
        self.base.element.click(self.collection_tab)

    def click_collection_box_1(self):
        self.base.element.click(self.collection_box_1)

    def check_collection(self):
        c_href = self.base.element.get_attribute_href(self.content_href_1)
        self.base.element.should_be_equal(self.photo_url, c_href)

    def click_create_collection_btn(self):
        self.base.element.click(self.create_collection_btn)

    def input_cc_title(self, title):
        self.base.element.send_keys(self.create_title_input_box, title)

    def click_cc_safe_btn(self):
        self.base.element.click(self.create_safe_btn)

    def get_creat_collection_box_href_1(self):
        return self.base.element.get_attribute_href(self.collection_box_1)

    def clear_collection_box_all(self):
        while self.base.element.ElementExist(self.collection_create_box):
            self.base.element.click(self.collection_box_del_btn)
            self.base.element.click(self.collection_box_del_yes)
            self.base.browser.refresh()


