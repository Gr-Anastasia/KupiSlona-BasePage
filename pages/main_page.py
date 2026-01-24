from pages.base_page import BasePage
from components.cart_product import CartProduct

class MainPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.driver = driver
        self.url = url

    def open(self):
        super().open()

    def get_product_by_title(self, title):
        return CartProduct(self.driver, title)

    def fill_count(self, title, count):
        product = self.get_product_by_title(title)
        product.fill_input_count_by_title(count)
        return product

