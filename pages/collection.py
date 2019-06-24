from pages.basepage import BasePage
from pages.personalpage import PersonalPage
from module.random_generator import RandomGenerator
import time


class Collection(BasePage):
    add_collection_btn = ('class', 'content-add-to-collection', 0)
    create_collection = ('class', 'create-new-collection', 0)
    input_box = ('class', 'ant-input-lg', 0)
    add_collection_box = ('class', 'collection-title', 0)
    submit_btn = ('class', 'submit-btn', 0)
    contained = ('class', 'contained', 0)
    collection_create_box = ('class', 'collection-create-box', 0)  # collection-create-box
    create_collection_btn = ('class', 'collection-create-btn', 0)  # 创建合辑btn
    create_explain = ('class', 'ant-form-explain', 0)  # 创建合辑-title错误提示框
    create_title_input_box = ('class', 'ant-input-lg', 0)  # 创建合辑-title输入框
    create_des_input_box = ('class', 'ant-input-lg', 1)  # 创建合辑-des输入框
    create_cancel_btn = ('class', 'cancel-btn', 0)  # 创建合辑-取消button
    create_safe_btn = ('class', 'save-btn', 0)  # 创建合辑-保存button
    cover_img = ('xpath', '//div[@class="collection-image-stumb"]/img', 0)
    collection_cover = ('class', 'collection-image-stumb', 0)  # 创建合辑-封面图设置
    thumb_input = ('class', 'thumb-input', 0)  # 创建合辑-封面图上传
    screenshot_save = ('class', 'ant-btn-primary', -1)  # 创建合辑-封面图保存
    privacy = ('class', 'ant-select-selection__rendered', 0)  # 可见性选择框
    privacy_select = ('class', 'ant-select-selection-selected-value', 0)
    privacy_public = ('class', 'ant-select-dropdown-menu-item', 0)
    privacy_personal = ('class', 'ant-select-dropdown-menu-item', 1)
    collection_edit_btn = ('class', 'edit', 0)  # 编辑合辑btn
    collection_box_del_btn = ('class', 'delete', 0)  # collection 删除button
    del_alert = ('class', 'ant-modal-body', 0)  # 删除弹窗
    del_yes = ('class', 'left-btn', 0)  # 删除-确认删除
    del_no = ('class', 'right-btn', 0)  # 删除-取消删除
    col_del_btn = ('xpath', '//div[@class="operation"]/img[2]', 0)  # collection 详情页删除button
    col_edit_btn = ('xpath', '//div[@class="operation"]/img[1]', 0)  # collection 详情页编辑button
    collection_box = ('xpath', '//div[@class="collection-title"]/a', 0)  # collection tab -第一个合辑
    content_href = ('xpath', '//div[@class="cover-bg"]/a', 0)  # collection box-第一个作品
    collection_box_title = ('xpath', '//div[@class="collection-title"]/a', 0)  # 合辑名称
    content_remove_btn = ('class', 'remove', 0)

    def __init__(self):
        super().__init__()
        self.content_url = None
        self.personal = PersonalPage()
        self.random = RandomGenerator()
        self.collection_name = None
        self.collection_des = None

    def get_current_content_url(self):
        self.content_url = self.window.get_current_url()

    def click_add_collection_btn(self):
        self.element.click(self.add_collection_btn)

    def add_collection(self):
        self.element.click(self.add_collection_box)

    def check_content_collected_in_detail_page(self):
        self.element.is_element_exist(self.contained)

    def check_content_removed_in_detail_page(self):
        self.element.is_element_not_exist(self.contained)

    def click_creat_collection_btn(self):
        self.element.click(self.create_collection)

    def input_collection_name(self):
        self.collection_name = self.random.random_comments(5)
        self.element.send_keys(self.input_box, self.collection_name)

    def click_create_and_add_btn(self):
        self.element.click(self.submit_btn)

    def click_collection_box(self):
        self.element.click(self.collection_box)

    def get_collection_box_name(self):
        self.collection_name = self.element.get_text(self.collection_box_title)

    def get_content_href(self):
        self.content_url = self.element.get_attribute_href(self.content_href)

    def check_content_collected_in_collection_box(self):
        self.click_collection_box()
        c_href = self.element.get_attribute_href(self.content_href)
        self.element.should_be_equal(self.content_url, c_href)

    def click_create_collection_btn(self):
        self.element.click(self.create_collection_btn)

    def click_edit_collection_btn(self):
        self.element.click(self.collection_edit_btn)

    def click_edit_btn_in_detail(self):
        self.element.click(self.col_edit_btn)

    def input_cc_title(self, title_length):
        self.collection_name = self.random.random_comments(title_length)
        self.element.double_click(self.create_title_input_box)
        self.element.backSpace(self.create_title_input_box)
        self.element.send_keys(self.create_title_input_box, self.collection_name)

    def input_cc_des(self, des_length):
        self.collection_des = self.random.random_comments(des_length)
        self.element.double_click(self.create_des_input_box)
        self.element.backSpace(self.create_des_input_box)
        self.element.send_keys(self.create_des_input_box, self.collection_des)

    def upload_cover(self):
        self.element.click(self.collection_cover)
        self.element.send_keys(self.thumb_input, '/Users/wangbo/PycharmProjects/automation/image/001.jpg')
        self.element.click(self.screenshot_save)

    def check_cover_img_replaced(self):
        self.element.is_element_exist(self.cover_img)

    def privacy_setting(self, type='public'):
        self.element.click(self.privacy)
        # self.element.click(self.privacy_list)
        if type == 'public':
            self.element.click(self.privacy_public)
        else:
            self.element.click(self.privacy_personal)

    def check_privacy_select_type(self, type='public'):
        title = self.element.get_attribute(self.privacy_select, 'title')
        if type == 'public':
            self.element.should_contains(title, '任何人都可以搜索和查看')
        else:
            self.element.should_contains(title, '知道链接的人才能观看')

    def click_cc_cancel_btn(self):
        self.element.click(self.create_cancel_btn)

    def click_cc_safe_btn(self):
        self.element.click(self.create_safe_btn)

    def create_collection_box(self, title_length, des_length, save=True):
        self.click_create_collection_btn()
        self.input_cc_title(title_length)
        self.input_cc_des(des_length)
        if save:
            self.click_cc_safe_btn()
        else:
            self.click_cc_cancel_btn()

    def check_create_collection_box_results(self, state=True):
        name = self.element.get_text(self.collection_box_title)
        if state:
            self.element.should_be_equal(name, self.collection_name)
        else:
            self.element.should_not_equal(name, self.collection_name)

    def check_collection_title_error_type(self, type):
        if type == 'empty':
            self.element.is_text_in_element(self.create_explain, '请输入标题, 请至少输入3个有效字符')
        elif type == 'less 3':
            self.element.is_text_in_element(self.create_explain, '请至少输入3个有效字符')
        else:
            print('no error')

    def edit_collection_box(self, enter='main', title_length=5, des_length=10):
        self.get_collection_box_name()
        if enter == 'main':
            self.click_edit_collection_btn()
        else:
            self.click_collection_box()
            self.click_edit_btn_in_detail()
        self.input_cc_title(title_length)
        self.input_cc_des(des_length)
        self.click_cc_safe_btn()

    def remove_collection_or_content(self, state=True):
        self.element.click(self.del_alert)
        if state:
            self.element.click(self.del_yes)
        else:
            self.element.click(self.del_no)

    def click_delete_btn(self):
        self.element.click(self.collection_box_del_btn)

    def click_delete_btn2(self):
        self.element.click(self.col_del_btn)

    def click_remove_btn(self):
        self.element.click(self.content_remove_btn)

    def check_remove_content_results(self, state=True):
        if state:
            if self.element.ElementExist(self.content_href):
                _href = self.element.get_attribute_href(self.content_href)
                self.element.should_not_equal(self.content_url, _href)
            else:
                self.element.is_element_not_exist(self.content_href)
        else:
            _href = self.element.get_attribute_href(self.content_href)
            self.element.should_be_equal(self.content_url, _href)

    def check_delete_collection_results(self, state=True):
        name = self.element.get_text(self.collection_box_title)
        if state:
            self.element.should_not_equal(self.collection_name, name)
        else:
            self.element.should_be_equal(self.collection_name, name)

    def clear_collection_box_all(self):
        while self.element.ElementExist(self.collection_create_box):
            self.click_delete_btn()
            self.remove_collection_or_content()
            time.sleep(2)
        self.element.is_element_not_exist(self.collection_create_box)
