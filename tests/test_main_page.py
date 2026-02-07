import allure

from playwright.sync_api import expect
from pages.base_page import BasePage
from pages.main_page import MainPage

@allure.title("Переход на страницу 'Игрушки' через верхнее меню в хэдере")
def test_header_menu(page):
    menu = BasePage(page, "https://kupislona-store.ru/")
    with allure.step("Открытие страницы https://kupislona-store.ru/"):
        menu.open()

    with allure.step("Нажать на пункт меню 'Игрушки'"):
        menu.get_header_menu_by_title("Игрушки").click()

        expect(page).to_have_url("https://kupislona-store.ru/katalog/igrushki")

@allure.title("Изменение количества через карточку товара в главном меню")
def test_cart_product(page):
    main = MainPage(page, "https://kupislona-store.ru/")
    with allure.step("Открытие страницы https://kupislona-store.ru/"):
        main.open()

    with allure.step("Изменить количество товара 'Серьги «Ace»' на 2 шт"):
        product = main.fill_count('Серьги «Ace»', "2")

    with allure.step("Нажать кнопку 'Купить'"):
        product.wrapper().get_by_role("button", name="Купить").click()

    messages_status = page.locator('//div[contains(@class, "messages status")]')

    expect(product.input_count().wrapper()).to_have_value("4")
    expect(messages_status).to_be_visible()













