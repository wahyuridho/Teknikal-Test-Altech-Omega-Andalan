from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from data import user_data as ud

class LoginPage(BasePage):
    URL = ud.base_url

    # Locators
    usernameInput = (By.ID, 'user-name')
    passwordInput = (By.ID, 'password')
    loginBtn = (By.ID, 'login-button')
    alertError = (By.XPATH, '//h3[@data-test="error"]')

    def open(self):
        self.driver.get(self.URL)

    def inputCredential(self, username, password):
        self.find_element(*self.usernameInput).send_keys(username)
        self.find_element(*self.passwordInput).send_keys(password)

    def submit(self):
        self.find_element(*self.loginBtn).click()

    def getErrorMessage(self):
        message = self.find_element(*self.alertError)
        return message.text