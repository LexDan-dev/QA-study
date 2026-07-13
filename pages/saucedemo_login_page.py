import re

from playwright.sync_api import Page, expect

# --- Константы: URL и локаторы (не в тестах!) ---
# saucedemo.com — тест-стенд для автоматизации (публичные креды)
LOGIN_URL = "https://www.saucedemo.com/"

USERNAME_SELECTOR = "#user-name"
PASSWORD_SELECTOR = "#password"
LOGIN_BUTTON_SELECTOR = "#login-button"
MENU_BUTTON_SELECTOR = "#react-burger-menu-btn"  # юзер-меню = признак входа
INVENTORY_URL = re.compile("inventory")  # URL после входа (аналог /dashboard)
ERROR_SELECTOR = "[data-test='error']"


class SauceDemoLoginPage:
    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto(LOGIN_URL)
        return self

    def login(self, username, password):
        self.page.locator(USERNAME_SELECTOR).fill(username)
        self.page.locator(PASSWORD_SELECTOR).fill(password)
        self.page.locator(LOGIN_BUTTON_SELECTOR).click()
        return self

    def should_be_logged_in(self):
        # приёмка: признак входа — URL содержит inventory И видно юзер-меню
        expect(self.page).to_have_url(INVENTORY_URL)
        expect(self.page.locator(MENU_BUTTON_SELECTOR)).to_be_visible()
        return self

    def should_show_error(self):
        expect(self.page.locator(ERROR_SELECTOR)).to_be_visible()
        return self
