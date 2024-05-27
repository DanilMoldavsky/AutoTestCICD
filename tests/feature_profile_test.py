from base.base_test import BaseTest

class ProfileFeatureTests(BaseTest):
    
    def test_change_profile_name(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.dashboard_page.is_opened()
        self.dashboard_page.click_my_info_link()
        self.personal_page.is_opened()
        self.personal_page.change_name("New Name")
        self.personal_page.save_change()
        self.personal_page.is_changes_saved()