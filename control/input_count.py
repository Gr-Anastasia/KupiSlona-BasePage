from control.base_control import BaseControl


class InputCount(BaseControl):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def wrapper(self):
        return self.driver.locator('//*[contains(@id, "edit-qty")]')
