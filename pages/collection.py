from pages.basepage import BasePage
from pages.personalpage import PersonalPage


class Collection(BasePage):
    add_collection_btn = ('class', 'content-add-to-collection', 0)
    add_collection_box = ('class', 'collection-title', 0)
    smoke_collection = ('link_text', 'smoke', 0)
    contained = ('class', 'contained', 0)
    collection_tab = ('class', ' tabs-tab', 2)  # 个人中心-collection tab
    create_collection_btn = ('class', 'collection-create-btn', 0)  # 创建合辑btn
    create_title_input_box = ('class', 'ant-input-lg', 0)  # 创建合辑-title输入框
    create_safe_btn = ('class', 'save-btn', 0)  # 创建合辑-保存button
    collection_create_box = ('class', 'collection-create-box', 0)  # collection-create-box
    collection_del_alert = ('class', 'ant-modal-body', 0)  # collection 删除弹窗
    collection_box_del_btn = ('class', 'delete', 0)  # collection 删除button
    collection_box_del_yes = ('class', 'left-btn', 0)  # collection 删除-确认删除
    collection_box_del_no = ('class', 'ant-btn-primary-ghost', 2)  # collection 删除-取消删除
    collection_box_1 = ('class', 'title', 1)  # collection tab -第一个合辑
    content_href_1 = ('class', 'title', 3)  # collection box-第一个作品

    def __init__(self):
        super().__init__()
        self.photo_url = None
        self.personal = PersonalPage()

    def go_collection_tab(self):
        self.personal.go_personal_page()
        self.element.click(self.collection_tab)

    def click_add_collection_btn(self):
        self.photo_url = self.window.get_current_url()
        self.element.click(self.add_collection_btn)

    def add_collection(self):
        self.element.click(self.add_collection_box)

    def check_collection_in_detail_page(self):
        self.element.is_element_exist(self.contained)

    def click_collection_tab(self):
        self.element.click(self.collection_tab)

    def click_collection_box_1(self):
        self.element.click(self.collection_box_1)

    def check_collection(self):
        c_href = self.element.get_attribute_href(self.content_href_1)
        self.element.should_be_equal(self.photo_url, c_href)

    def click_create_collection_btn(self):
        self.element.click(self.create_collection_btn)

    def input_cc_title(self, title):
        self.element.send_keys(self.create_title_input_box, title)

    def click_cc_safe_btn(self):
        self.element.click(self.create_safe_btn)

    def get_creat_collection_box_href_1(self):
        return self.element.get_attribute_href(self.collection_box_1)

    def clear_collection_box_all(self):
        while self.element.ElementExist(self.collection_create_box):
            self.element.click(self.collection_box_del_btn)
            self.element.click(self.collection_del_alert)
            self.element.click(self.collection_box_del_yes)
            self.browser.refresh()
