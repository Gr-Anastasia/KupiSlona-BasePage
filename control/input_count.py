from control.base_control import BaseControl


class InputCount(BaseControl):
    def __init__(self, page):
        super().__init__(page)
        self.page = page

    def wrapper(self):
        return self.page.locator('[id*="edit-qty"]')
