# tests/test_login.py
from pages.login_page import LoginPage

def test_login_sukses(page):
    login = LoginPage(page)
    login.goto()
    login.login("test", "test")
    assert "/login" not in page.url

def test_login_gagal(page):
    login = LoginPage(page)
    login.goto()
    login.login("salah@email.com", "passwordsalah")
    error = login.get_error_message()
    assert error.is_visible()
    assert "Wrong login/password" in error.inner_text()