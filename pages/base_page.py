class BasePage:
    def __init__(self, page, url):
        self.page = page
        self.url = url

    def open(self):
        self.page.goto(self.url)

    def header(self):
        self.page.locator('[id*="header"]')

    def get_header_menu_by_title(self, title):
        return self.page.locator('[id*="superfish-1"]').get_by_role("link", name=title)

    def footer(self):
        self.page.locator('[id*="footer-wrapper"]')
