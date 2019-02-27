from pages.basepage import BasePage
from pages.personalpage import PersonalPage
from module.random_generator import RandomGenerator


class Collection(BasePage):
    add_collection_btn = ('class', 'content-add-to-collection', 0)
    add_collection_box = ('class', 'collection-title', 0)
    contained = ('class', 'contained', 0)
    create_collection_btn = ('class', 'collection-create-btn', 0)  # 创建合辑btn
    create_title_input_box = ('class', 'ant-input-lg', 0)  # 创建合辑-title输入框
    create_safe_btn = ('class', 'save-btn', 0)  # 创建合辑-保存button
    collection_create_box = ('class', 'collection-create-box', 0)  # collection-create-box
    collection_del_alert = ('class', 'ant-modal-body', 0)  # collection 删除弹窗
    collection_box_del_btn = ('class', 'delete', 0)  # collection 删除button
    collection_box_del_yes = ('class', 'left-btn', 0)  # collection 删除-确认删除
    collection_box_del_no = ('class', 'ant-btn-primary-ghost', 2)  # collection 删除-取消删除
    collection_box = ('xpath', '//div[@class="play-overlay"]/a', 0)   # collection tab -第一个合辑
    content_href = ('xpath', '//div[@class="cover-bg"]/a', 0)  # collection box-第一个作品
    collection_box_title = ('xpath', '//div[@class="collection-title"]/a', 0)

    def __init__(self):
        super().__init__()
        self.photo_url = None
        self.personal = PersonalPage()
        self.random = RandomGenerator()
        self.collection_name = None

    def click_add_collection_btn(self):
        self.photo_url = self.window.get_current_url()
        self.element.click(self.add_collection_btn)

    def add_collection(self):
        self.element.click(self.add_collection_box)

    def check_collection_in_detail_page(self):
        self.element.is_element_exist(self.contained)

    def click_collection_box_1(self):
        self.element.click(self.collection_box)

    def check_collection(self):
        c_href = self.element.get_attribute_href(self.content_href)
        self.element.should_be_equal(self.photo_url, c_href)

    def click_create_collection_btn(self):
        self.element.click(self.create_collection_btn)

    def input_cc_title(self):
        self.collection_name = self.random.random_comments(8)
        self.element.send_keys(self.create_title_input_box, self.collection_name)

    def click_cc_safe_btn(self):
        self.element.click(self.create_safe_btn)

    def check_created_collection(self):
        name = self.element.get_text(self.collection_box_title)
        self.element.should_be_equal(name, self.collection_name)

    def clear_collection_box_all(self):
        while self.element.ElementExist(self.collection_create_box):
            self.element.click(self.collection_box_del_btn)
            self.element.click(self.collection_del_alert)
            self.element.click(self.collection_box_del_yes)
            self.browser.refresh()
