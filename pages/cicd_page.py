from playwright.sync_api import Page

HERO_GRID = "Hero-grid"
CONTACT_SALES_LINK = "Contact sales"


class CiCdPage:
    def __init__(self, page: Page):
        self.page = page

    def click_contact_sales(self):
        self.page.get_by_test_id(HERO_GRID).get_by_role(
            "link", name=CONTACT_SALES_LINK
        ).click()
        return self
