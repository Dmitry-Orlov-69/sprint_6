import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def navigate_to_main_page(driver):
    driver.get("https://qa-scooter.praktikum-services.ru")
    yield driver  # Передаём драйвер дальше, чтобы тесты могли его использовать