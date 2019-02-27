from robot.api.deco import keyword
from pages.collection import Collection
from pages.basepage import BasePage
from services.CommonLibrary import CommonLibrary
from services.PhotoLibrary import PhotoLibrary
from services.PersonalLibrary import PersonalLibrary


class CollectionLibrary(object):
    def __init__(self):
        self.collection = Collection()
        self.base = BasePage()
        self.common = CommonLibrary()
        self.photo = PhotoLibrary()
        self.personal = PersonalLibrary()

    @keyword
    def go_collection_tab(self):
        self.personal.go_personal_center()
        self.personal.switch_nav_tab('合辑')

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
        self.go_collection_tab()
        self.collection.click_collection_box_1()
        self.collection.check_collection()

    @keyword
    def create_collection(self):
        self.collection.click_create_collection_btn()
        self.collection.input_cc_title()
        self.collection.click_cc_safe_btn()

    @keyword
    def Check_the_collection_was_created_successfully(self):
        self.collection.check_created_collection()

    @keyword
    def clear_collection_box_all(self):
        self.collection.clear_collection_box_all()
