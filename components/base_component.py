from playwright.sync_api import expect

class BaseComponent:
    def __init__(self, driver):
        self.driver = driver

    def is_visible(self):
        return expect(self.driver).to_be_visible()