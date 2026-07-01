from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://example.com/login"

    def open(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        self.driver.type("username", username)
        self.driver.type("password", password)
        self.driver.click("login-btn")
