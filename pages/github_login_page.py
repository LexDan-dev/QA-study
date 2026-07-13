from playwright.sync_api import Page, expect

# --- Константы: URL и локаторы ---
LOGIN_URL = "https://github.com/login"

USERNAME_SELECTOR = "#login_field"
PASSWORD_SELECTOR = "#password"
SIGN_IN_SELECTOR = "input[name='commit']"
ERROR_SELECTOR = ".flash-error"
ERROR_TEXT = "Incorrect username or password"
USER_MENU_LABEL = "View profile and more"


class GitHubLoginPage:
    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto(LOGIN_URL)
        return self

    def login(self, username, password):
        self.page.locator(USERNAME_SELECTOR).fill(username)
        self.page.locator(PASSWORD_SELECTOR).fill(password)
        self.page.locator(SIGN_IN_SELECTOR).click()
        return self

    def should_show_error(self):
        # контейнер ошибки, отобранный по тексту (на странице есть пустые .flash-error)
        error = self.page.locator(ERROR_SELECTOR, has_text=ERROR_TEXT)
        expect(error).to_be_visible()  # ждём появления (без sleep)
        return self

    def should_be_logged_in(self):
        expect(self.page.get_by_label(USER_MENU_LABEL)).to_be_visible()
        return self
