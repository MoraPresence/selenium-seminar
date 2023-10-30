from ui.locators import basic_locators
from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage


class LoginPage(BasePage):
    url = 'https://park.vk.company/'
    locators = basic_locators.LoginPageLocators()

    def login(self, user, password):
        self.driver.get(self.url)

        self.click(self.locators.OPEN_LOGIN)
        self.find(self.locators.LOGIN).send_keys(user)
        self.find(self.locators.PASSWORD).send_keys(password)
        self.click(self.locators.SUBMIT)

        return MainPage(self.driver)
