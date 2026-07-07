from selene import browser, have


def test_login_page_opens(driver):
    browser.open("https://the-internet.herokuapp.com/login")
    browser.element("h2").should(have.text("Login Page"))
