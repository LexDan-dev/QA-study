from playwright.sync_api import Page

FIRST_NAME = "First name"
LAST_NAME = "Last name"


class ContactSalesPage:
    def __init__(self, page: Page):
        self.page = page

    def fill_form(self, first_name, last_name):
        self.page.wait_for_load_state("networkidle")
        self.page.get_by_role("textbox", name=FIRST_NAME).fill(first_name)
        self.page.get_by_role("textbox", name=LAST_NAME).fill(last_name)
        return self

    def get_field_value(self, field):
        names = {"first": FIRST_NAME, "last": LAST_NAME}
        return self.page.get_by_role("textbox", name=names[field]).input_value()
