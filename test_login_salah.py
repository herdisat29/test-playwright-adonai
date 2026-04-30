def test_login_gagal(page):
    page.goto("http://192.168.10.72:10018/odoo")
    page.fill("#login", "salah@email.com")
    page.fill("#password", "passwordsalah")
    page.click("button[type='submit']")
    page.wait_for_load_state("load")

    # Pakai class yang lo temuin dari inspect
    error_message = page.locator("p.alert.alert-danger")
    error_message.wait_for(state="visible")
    
    # Cek keliatan
    assert error_message.is_visible()
    
    # Bonus: cek juga isi teksnya bener
    assert "Wrong login/password" in error_message.inner_text()