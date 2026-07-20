from playwright.sync_api import Page

CICD_LINK = "CI/CD"


class SolutionsMenu:
    def __init__(self, page: Page):
        self.page = page

    def select_cicd(self):
        # .first — если "CI/CD" встречается несколько раз (dropdown + страница)
        self.page.get_by_role("link", name=CICD_LINK).first.click()
        return self
