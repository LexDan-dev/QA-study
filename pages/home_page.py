from playwright.sync_api import Page

HOME_URL = "https://github.com/"
SOLUTIONS_BUTTON = "Solutions"


class HomePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto(HOME_URL)
        return self

    def go_to_solutions(self):
        self.page.get_by_role("button", name=SOLUTIONS_BUTTON).click()
        return self
