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
        self.cl = CommonLibrary()
        self.pp = PhotoLibrary()
        self.per = PersonalLibrary()

    @keyword
    def add_photo_collection(self):
        self.cl.go_page('全景图')
        self.pp.go_photo_detail()
        self.collection.click_add_collection_btn()
        self.collection.add_collection()
        self.collection.click_add_collection_btn()

    @keyword
    def check_collection(self):
        self.collection.check_collection_in_detail_page()
        self.cl.go_page('合辑')
        self.collection.click_collection_box_1()
        self.collection.check_collection()

    @keyword
    def create_collection(self, title):
        self.collection.click_create_collection_btn()
        self.collection.input_cc_title(title)
        self.collection.click_cc_safe_btn()
        collection_href = self.collection.get_creat_collection_box_href_1()
        self.base.element.should_contains(collection_href, title)

    @keyword
    def clear_collection_box_all(self):
        self.collection.clear_collection_box_all()
