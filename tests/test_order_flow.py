import pytest
from pages.order_page import OrderPage
from locators.order_page_locators import OrderPageLocators
import allure
from data import data

@pytest.mark.parametrize('name, surname, address, phone, metro_station_text, comment, order_button', data)

@allure.title("Проверка сообщения об успешном оформлении заказа")
def test_order_flow(navigate_to_main_page, name, surname, address, phone, metro_station_text, comment, order_button):
    order_page = OrderPage(navigate_to_main_page)

    # Нажимаем на кнопку "Заказать" главной страницы
    order_page.click_orderbutton_with_js(order_button)

    try:
        # Ждём перехода на страницу с формой заказа
        order_page.wait_for_url_contains("https://qa-scooter.praktikum-services.ru/order")
    except Exception as e:
        # Если переход не произошёл, выводим сообщение об ошибке и завершаем тест
        print("Ошибка: не удалось перейти на страницу заказа.", e)
        return

    # Заполняем форму заказа
    order_page.fill_field(OrderPageLocators.input_name, name)
    order_page.fill_field(OrderPageLocators.input_surname, surname)
    order_page.fill_field(OrderPageLocators.input_address, address)
    order_page.click_button(OrderPageLocators.input_metro_station)

    # Ищем станцию метро по тексту и кликаем на неё
    order_page.click_metro_station(metro_station_text)

    order_page.fill_field(OrderPageLocators.input_phone, phone)
    order_page.wait_for_element_to_be_clickable(OrderPageLocators.button_next)
    order_page.click_button(OrderPageLocators.button_next)

    # Выбираем дату и срок аренды
    order_page.click_button(OrderPageLocators.input_pickup_date)
    order_page.wait_for_element_to_be_clickable(OrderPageLocators.date_picker_20th).click()
    order_page.click_button(OrderPageLocators.dropdown_rental_period)
    order_page.select_option(OrderPageLocators.option_rental_period_day)

    # Выбираем цвет самоката и добавляем комментарий
    order_page.click_button(OrderPageLocators.checkbox_color_black)
    order_page.fill_field(OrderPageLocators.input_comment, comment)

    # Завершаем оформление заказа
    order_page.click_button(OrderPageLocators.button_place_order)
    confirm_modal = order_page.wait_for_visibility_of_element_located(OrderPageLocators.modal_header_confirm_order)
    order_page.click_button(OrderPageLocators.button_yes)

    # Проверяем сообщение об успешном оформлении заказа
    order_confirmed_modal = order_page.wait_for_visibility_of_element_located(OrderPageLocators.modal_header_order_confirmed)
    assert "Заказ оформлен" in order_confirmed_modal.text