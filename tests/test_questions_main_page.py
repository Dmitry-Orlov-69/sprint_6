import pytest
from pages.main_page import MainPage
import allure
from data import questions_data

@pytest.mark.parametrize("question_button, expected_text, answer_locator", questions_data)
@allure.title("Проверка ответа на вопрос: {question_button}")
def test_questions(navigate_to_main_page, question_button, expected_text, answer_locator):
    main_page = MainPage(navigate_to_main_page)

    # Прокручиваем элемент в видимую область
    main_page.scroll_into_view(question_button)

    # Кликаем по элементу с использованием JavaScript
    main_page.click_button_with_js(question_button)

    # Добавляем ожидание появления текста ответа
    main_page.wait_for_text_to_be_present_in_element(answer_locator, expected_text)

    answer = main_page.get_answer_text(answer_locator)
    assert answer == expected_text