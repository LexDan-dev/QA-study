import pytest


@pytest.fixture
def general_fixture():
    return "фикстура из conftest.py"


class FakeDriver:
    """Заглушка вместо браузера для учебных POM-тестов (имитирует Selenium)."""

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


@pytest.fixture
def fake_driver():
    return FakeDriver()
