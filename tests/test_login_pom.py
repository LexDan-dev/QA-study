from study_cases.pom_demo import FakeDriver, LoginPage


def test_login_success():
    driver = FakeDriver()
    page = LoginPage(driver)
    page.open()
    page.login("user", "pass")
    assert driver.logged_in is True


def test_login_fail():
    driver = FakeDriver()
    page = LoginPage(driver)
    page.open()
    page.login("user", "")
    assert driver.logged_in is False
