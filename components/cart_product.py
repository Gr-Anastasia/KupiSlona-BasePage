from components.base_component import BaseComponent
from control.input_count import InputCount


class CartProduct(BaseComponent):
    def __init__(self, driver, title):
        super().__init__(driver)
        self.driver = driver
        self.title = title

    def wrapper(self):
        return self.driver.locator(f'//a[contains(text(), "{self.title}")]/ancestor::li')

    def input_count(self):
        return InputCount(self.wrapper())

    def fill_input_count_by_title(self, count):
        self.input_count().wrapper().fill(count)
