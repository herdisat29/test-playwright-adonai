def test_login_adonai(page):
    page.goto("http://192.168.10.72:10018/odoo")
    page.fill("#login","test")
    page.fill("#password","test")
    page.click("button[type='submit']")
    page.wait_for_load_state("load")
    page.pause()

