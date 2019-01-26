from robot.api.deco import keyword
from pages.settingspage import SettingsPage


class SettingsLibrary(object):
    def __init__(self):
        self.setting = SettingsPage()

    @keyword
    def should_be_settings_page(self):
        self.setting.is_settings_page()

    @keyword
    def go_settings_page(self):
        self.setting.go_settings_page()

    @keyword
    def edit_user_information(self, _name, _username, _des):
        self.setting.input_name(_name)
        self.setting.input_username(_username)
        self.setting.input_description(_des)
        self.setting.click_save_btn()

    @keyword
    def check_user_information_was_modified_successfully(self, _name, _username, _des):
        self.setting.is_edit(_name, _username, _des)
