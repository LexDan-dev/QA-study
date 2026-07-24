import pytest
import requests
from dotenv import load_dotenv
from selenium import webdriver
from selene import browser
from playwright.sync_api import sync_playwright

load_dotenv()  # читает .env → переменные доступны через os.getenv


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


@pytest.fixture(scope="function")
def driver():
    chrome = webdriver.Chrome()
    browser.config.driver = chrome
    browser.config.timeout = 4
    yield chrome
    chrome.quit()


@pytest.fixture
def page():
    with sync_playwright() as pw:
        chromium = pw.chromium.launch(headless=False)  # headed → окно видно
        new_page = chromium.new_page()
        yield new_page  # здесь бежит тест
        chromium.close()  # teardown: закрыть браузер


@pytest.fixture
def session():
    with requests.Session() as s:
        yield s  # одна сессия на тест, закроется автоматически
