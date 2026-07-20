import pytest
from playwright.sync_api import Page

from pages.home_page import HomePage
from pages.solutions_menu import SolutionsMenu
from pages.cicd_page import CiCdPage
from pages.contact_sales_page import ContactSalesPage

pytestmark = pytest.mark.ui

FIRST_NAME = "Alex"
LAST_NAME = "Skvortsov"


def test_contact_sales_form(page: Page):
    HomePage(page).open().go_to_solutions()  # шаги 1–2 флоу
    SolutionsMenu(page).select_cicd()  # шаг 2–3
    CiCdPage(page).click_contact_sales()  # шаг 3–4
    form = ContactSalesPage(page)
    form.fill_form(FIRST_NAME, LAST_NAME)  # шаг 4

    # приёмка: значения в полях совпадают с переданными
    assert form.get_field_value("first") == FIRST_NAME
    assert form.get_field_value("last") == LAST_NAME
