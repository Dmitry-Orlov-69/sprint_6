from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_url_contains(self, url_part, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.url_contains(url_part))