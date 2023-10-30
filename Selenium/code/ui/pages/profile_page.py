from ui.locators import basic_locators
from ui.pages.base_page import BasePage


class ProfileSettingsPage(BasePage):
    url = 'https://park.vk.company/cabinet/settings/'

    locators = basic_locators.ProfileSettingsPageLocators()

    def change_about(self, m_about: str):
        about = self.find(self.locators.ABOUT)
        about.clear()
        about.send_keys(m_about)
        self.click(self.locators.SUBMIT)

    def get_about(self):
        return self.find(self.locators.ABOUT).text
