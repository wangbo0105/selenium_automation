from robot.api.deco import keyword
from pages.settingspage import Settingspage
from services.CommonLibrary import CommonLibrary


class SettingsLibrary(Settingspage):
    cl = CommonLibrary()
    _name1 = 'name1'
    _username1 = 'username1'
    _des1 = 'description1'
    _website1 = 'http://www.veer.com'

    @keyword
    def go_settings_page(self):
        self.cl.goto_page_by_hover(self.user_tab, self.setting)

    @keyword
    def is_settings_page(self):
        self.is_text_in_url('settings')
        self.isElementExist(self.page_title)

    @keyword
    def edit_data(self, _name1, _username1, _des1):
        self.input_name(_name1)
        self.input_username(_username1)
        self.input_description(_des1)
        self.click_save_btn()

    @keyword
    def is_edit(self, _name1, _username1, _des1, value='value'):
        self.is_input_text(self.name, value, _name1)
        self.is_input_text(self.username, value, _username1)
        self.is_input_text(self.personal_description, value,  _des1)


