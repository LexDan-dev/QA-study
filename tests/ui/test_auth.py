import os

import pytest
from playwright.sync_api import Page

from pages.saucedemo_login_page import SauceDemoLoginPage
from pages.github_login_page import GitHubLoginPage

pytestmark = pytest.mark.ui  # все тесты файла — маркер ui

# saucedemo — публичные тест-креды (позитивный поток)
SAUCE_USER = "standard_user"
SAUCE_PASS = "secret_sauce"

# github — заведомо неверные креды для негатива (логин без подчёркиваний!)
GH_INVALID_USER = "Lexar996"
GH_INVALID_PASS = "wrongpass123"

# github — реальные креды для позитива (только из .env, не в коде)
GH_USER = os.getenv("GH_USER")
GH_PASS = os.getenv("GH_PASS")


def test_login_success(page: Page):
    # позитив: вход валидными → приёмка (URL /inventory + юзер-меню)
    SauceDemoLoginPage(page).open().login(SAUCE_USER, SAUCE_PASS).should_be_logged_in()


def test_login_fail(page: Page):
    # негатив: неверные креды → контейнер ошибки (ждём через expect)
    GitHubLoginPage(page).open().login(
        GH_INVALID_USER, GH_INVALID_PASS
    ).should_show_error()


@pytest.mark.skipif(
    not (GH_USER and GH_PASS),
    reason="нет GH_USER/GH_PASS; реальный вход на github не автоматизируем (2FA/ToS)",
)
def test_github_login_success(page: Page):
    GitHubLoginPage(page).open().login(GH_USER, GH_PASS).should_be_logged_in()
