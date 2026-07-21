import pytest
from playwright.sync_api import Page

from pages.duckduckgo_search_page import DuckDuckGoSearchPage

pytestmark = pytest.mark.ui


@pytest.mark.parametrize("query", ["qa", "aqa", "python"])
def test_search_returns_results(page: Page, query):
    DuckDuckGoSearchPage(page).open().search(query).should_have_more_than(5)
