from pages.login_page import LoginPage


def test_login_success(fake_driver):
    page = LoginPage(fake_driver)
    page.open()
    page.login("user", "pass")
    assert fake_driver.logged_in is True


def test_login_fail(fake_driver):
    page = LoginPage(fake_driver)
    page.open()
    page.login("user", "")
    assert fake_driver.logged_in is False
