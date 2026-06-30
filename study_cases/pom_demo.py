class FakeDriver:
    def __init__(self):
        self.current_url = None
        self._fields = {}
        self.logged_in = False

    def get(self, url):  # ~ Selenium: driver.get(url)
        self.current_url = url

    def type(self, field, text):  # ~ find_element(...).send_keys(text)
        self._fields[field] = text

    def click(self, button):  # ~ find_element(...).click()
        creds_filled = self._fields.get("username") and self._fields.get("password")
        if button == "login-btn" and creds_filled:
            self.logged_in = True


class BasePage:
    def __init__(self, driver):
        self.driver = driver


class LoginPage(BasePage):
    URL = "https://example.com/login"

    def open(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        self.driver.type("username", username)
        self.driver.type("password", password)
        self.driver.click("login-btn")
