from pages.login_page import LoginPage

def test_halaman_setelah_login(page):
    login = LoginPage(page)
    login.goto()
    login.login("test", "test")

    # Verifikasi 1: URL berubah dari /login
    assert "/login" not in page.url

    # Verifikasi 2: Halaman bukan login page lagi
    assert not page.get_by_role("button", name="Log in").is_visible()

    # Verifikasi 3: Salah satu menu utama keliatan
    assert page.locator(".o_main_navbar").is_visible()