from playwright.sync_api import expect

class BaseComponent:
    def __init__(self, page):
        self.page = page

    def is_visible(self):
        return expect(self.page).to_be_visible()