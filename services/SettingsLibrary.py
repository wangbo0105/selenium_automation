from robot.api.deco import keyword
from pages.settingspage import Settingspage
from services.CommonLibrary import CommonLibrary


class SettingsLibrary(Settingspage):
    cl = CommonLibrary()

    @keyword
    def go_settings_page(self):
        self.cl.goto_page_by_hover(self.user_tab, self.setting)

    @keyword
    def is_settings_page(self):
        self.is_text_in_url('settings')
        self.isElementExist(self.page_title)

    @keyword
    def edit_data(self, _name, _username, _des):
        self.input_name(_name)
        self.input_username(_username)
        self.input_description(_des)
        self.click_save_btn()

    @keyword
    def is_edit(self, _name, _username, _des, value='value'):
        self.is_input_text(self.name, value, _name)
        self.is_input_text(self.username, value, _username)
        self.is_input_text(self.personal_description, value,  _des)


