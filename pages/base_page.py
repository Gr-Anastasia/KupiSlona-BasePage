class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.goto(self.url)

    def header(self):
        self.driver.locator('//*[@id = "header"]')

    def get_header_menu_by_title(self, title):
        return self.driver.locator('//*[@id="superfish-1"]').get_by_role("link", name=title)

    def footer(self):
        self.driver.locator('//*[@id = "footer-wrapper"]')
