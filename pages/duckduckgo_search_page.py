from playwright.sync_api import Page, expect

# --- Константы: URL и локаторы ---
SEARCH_URL = "https://duckduckgo.com/"

SEARCH_INPUT = "#searchbox_input"
RESULT = '[data-testid="result"]'


class DuckDuckGoSearchPage:
    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto(SEARCH_URL)
        return self

    def search(self, query):
        box = self.page.locator(SEARCH_INPUT)
        box.fill(query)
        box.press("Enter")
        return self

    def should_have_more_than(self, count, timeout=15000):
        expect(self.page.locator(RESULT).nth(count)).to_be_visible()
        return self
