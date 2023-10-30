from selenium.webdriver.common.by import By


class LoginPageLocators(BasePageLocators):
    OPEN_LOGIN = (By.LINK_TEXT, 'Войти')
    LOGIN = (By.XPATH, "//input[@name='login' and @type='text']")
    PASSWORD = (By.XPATH, "//input[@name='password' and @type='password']")
    SUBMIT = (By.NAME, "submit_login")
    ERROR_MESSAGE = (By.CLASS_NAME, "validate-error-login")


class ProfilePageLocators(BasePageLocators):
    ABOUT = (By.ID, "profile_about")
    SUBMIT = (By.NAME, "submit_profile_edit")
