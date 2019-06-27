from robot.api.deco import keyword
from pages.collection import Collection
from pages.basepage import BasePage
from services.CommonLibrary import CommonLibrary
from services.PersonalLibrary import PersonalLibrary
from services.HomeLibrary import HomeLibrary
from services.PhotoLibrary import PhotoLibrary
import time


class CollectionLibrary(object):
    def __init__(self):
        self.collection = Collection()
        self.base = BasePage()
        self.common = CommonLibrary()
        self.home = HomeLibrary()
        self.personal = PersonalLibrary()
        self.photo = PhotoLibrary()

    @keyword
    def go_collection_tab(self):
        self.personal.go_personal_center()
        self.personal.switch_nav_tab('合辑')

    @keyword
    def go_collection_box_detail(self):
        self.collection.click_collection_box()

    @keyword
    def create_collection_and_add_content(self):
        self.personal.view_own_content()
        self.collection.get_current_content_url()
        self.collection.click_add_collection_btn()
        self.collection.click_creat_collection_btn()
        self.collection.input_collection_name()
        self.collection.click_create_and_add_btn()

    @keyword
    def add_content_to_collection(self):
        self.personal.view_own_content()
        self.collection.get_current_content_url()
        self.collection.click_add_collection_btn()
        self.collection.add_collection()
        self.collection.click_add_collection_btn()

    # @keyword
    # def remove_content_in_content_detail(self):
    #     self.common.go_page('home')
    #     self.home.click_feeds_content_item('精选图片')
    #     self.collection.get_current_content_url()
    #     self.collection.click_add_collection_btn()
    #     self.collection.add_collection()
    #     self.collection.click_add_collection_btn()

    @keyword
    def check_content_has_collected(self):
        self.collection.check_content_collected_in_detail_page()
        self.go_collection_tab()
        self.collection.check_content_collected_in_collection_box()

    @keyword
    def check_content_has_removed_from_content_detail(self):
        self.collection.check_content_removed_in_detail_page()
        self.go_collection_tab()
        self.collection.click_collection_box()
        self.collection.check_remove_content_results()

    @keyword
    def create_collection_box(self, save=True, title_length=5, des_length=10):
        self.collection.create_collection_box(title_length, des_length, save)

    @keyword
    def cancel_create_collection_page(self):
        self.collection.click_cc_cancel_btn()

    @keyword
    def check_create_collection_box_results(self, state=True):
        time.sleep(2)
        self.collection.check_create_collection_box_results(state)

    @keyword
    def check_collection_title_error_type(self, type):
        self.collection.check_collection_title_error_type(type)

    @keyword
    def switch_privacy_type(self, type):
        self.collection.click_create_collection_btn()
        self.collection.privacy_setting(type)

    @keyword
    def check_privacy_select_type(self, type):
        self.collection.check_privacy_select_type(type)

    # @keyword
    # def upload_cover(self):
    #     self.collection.click_create_collection_btn()
    #     self.collection.upload_cover()
    #
    # @keyword
    # def check_cover_replaced(self):
    #     self.collection.check_cover_img_replaced()

    @keyword
    def edit_collection(self, enter='main'):
        self.collection.edit_collection_box(enter)

    @keyword
    def remove_content_from_collection_detail(self, state=True):
        self.collection.click_collection_box()
        self.collection.get_content_href()
        self.collection.click_remove_btn()
        self.collection.remove_collection_or_content(state)

    @keyword
    def check_remove_content_results(self, state=True):
        self.collection.check_remove_content_results(state)

    @keyword
    def delete_collection_box(self, state=True):
        self.collection.get_collection_box_name()
        self.collection.click_delete_btn()
        self.collection.remove_collection_or_content(state)

    @keyword
    def delete_collection_box_in_detail(self, state=True):
        self.collection.get_collection_box_name()
        self.collection.click_collection_box()
        self.collection.click_delete_btn2()
        self.collection.remove_collection_or_content(state)

    @keyword
    def remove_content_from_collection(self):
        self.collection.click_collection_box()

    @keyword
    def check_delete_collection_results(self, state=True):
        self.collection.check_delete_collection_results(state)

    @keyword
    def clear_collection_box_all(self):
        self.collection.clear_collection_box_all()
