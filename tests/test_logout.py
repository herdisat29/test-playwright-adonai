    # tests/test_logout.py
from pages.login_page import LoginPage

def test_logout(page):
    login = LoginPage(page)
    login.goto()
    login.login("test", "test")

    page.get_by_role("button", name="User").click()
    page.get_by_role("menuitem", name="Log out").click()
    page.wait_for_load_state("load")

    assert "/login" in page.url
    assert page.locator("button[type='submit']").is_visible()