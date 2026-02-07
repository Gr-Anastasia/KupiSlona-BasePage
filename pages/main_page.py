from pages.base_page import BasePage
from components.cart_product import CartProduct

class MainPage(BasePage):
    def __init__(self, page, url):
        super().__init__(page, url)
        self.page = page
        self.url = url

    def open(self):
        super().open()

    def get_product_by_title(self, title):
        return CartProduct(self.page, title)

    def fill_count(self, title, count):
        product = self.get_product_by_title(title)
        product.fill_input_count_by_title(count)
        return product

