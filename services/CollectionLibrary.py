from robot.api.deco import keyword
from pages.collection import Collection
from pages.basepage import BasePage
from services.CommonLibrary import CommonLibrary
from services.PhotoLibrary import PhotoLibrary


class CollectionLibrary(object):
    def __init__(self):
        self.collection = Collection()
        self.base = BasePage()
        self.common = CommonLibrary()
        self.photo = PhotoLibrary()

    @keyword
    def go_collection_tab(self):
        self.collection.go_collection_tab()

    @keyword
    def add_photo_collection(self):
        self.common.go_page('photo')
        self.photo.photo_click_item('photo_content')
        self.collection.click_add_collection_btn()
        self.collection.add_collection()
        self.collection.click_add_collection_btn()

    @keyword
    def check_collection(self):
        self.collection.check_collection_in_detail_page()
        self.collection.go_collection_tab()
        self.collection.click_collection_box_1()
        self.collection.check_collection()

    @keyword
    def create_collection(self, title):
        self.collection.click_create_collection_btn()
        self.collection.input_cc_title(title)
        self.collection.click_cc_safe_btn()

    @keyword
    def Check_the_collection_was_created_successfully(self, title):
        collection_href = self.collection.get_creat_collection_box_href_1()
        self.base.element.should_contains(collection_href, title)

    @keyword
    def clear_collection_box_all(self):
        self.collection.clear_collection_box_all()
