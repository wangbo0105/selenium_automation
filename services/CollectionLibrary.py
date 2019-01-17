from robot.api.deco import keyword
from pages.collection import Collection
from services.PhotoLibrary import PhotoLibrary
from services.PersonalLibrary import PersonalLibrary


class CollectionLibrary(Collection):
    pp = PhotoLibrary()
    per = PersonalLibrary()
    photo_url = None

    @keyword
    def add_photo_collection(self):
        self.pp.go_photo()
        self.pp.go_photo_detail()
        self.click_add_collection_btn()
        self.add_collection()
        self.photo_url = self.get_current_url()

    @keyword
    def check_collection_in_detail_page(self):
        self.is_element_exist(self.contained)
        self.click_add_collection_btn()

    @keyword
    def go_collection_tab(self):
        self.per.go_personal()
        self.click_collection_tab()

    @keyword
    def go_collection_box(self):
        self.click_collection_box_1()

    @keyword
    def check_collection_in_collection_box(self):
        self.should_be_equal(self.photo_url, self.get_content_href_1())

    @keyword
    def create_collection(self, title):
        self.click_create_collection()
        self.input_cc_title(title)
        self.click_cc_safe_btn()
        collection_href = self.get_collection_box_href_1()
        self.should_contains(collection_href, title)
