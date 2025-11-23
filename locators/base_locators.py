from selenium.webdriver.common.by import By

class BaseLocators:
    logo_scooter = (By.XPATH, "//img[@src='/assets/scooter.svg']") # логотип "Самоката"
    logo_yandex = (By.XPATH, "//img[@src='/assets/ya.svg']") # логотип "Яндекса" 