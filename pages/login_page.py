class LoginPage:
    def __init__(self, page):
        self.page = page
        self.url = "http://192.168.10.72:10018/odoo"

    def goto(self):
        self.page.goto(self.url)

    def login(self, username, password):
        self.page.fill("#login", username)
        self.page.fill("#password", password)
        self.page.click("button[type='submit']")
        self.page.wait_for_load_state("load")

    def get_error_message(self):
        return self.page.locator("p.alert.alert-danger")