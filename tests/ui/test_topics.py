import pytest
from playwright.sync_api import Page

from pages.github_topics_page import GitHubTopicsPage

pytestmark = pytest.mark.ui

EXPECTED_TOPICS = {"javascript", "typescript", "react", "chrome"}


def test_topics_section_contains_expected(page: Page):
    topics = GitHubTopicsPage(page).open()
    topics.should_have_topics_section()

    actual = topics.get_topic_slugs()
    missing = EXPECTED_TOPICS - actual
    assert not missing, f"нет ожидаемых топиков: {missing}"
