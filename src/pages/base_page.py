from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class BasePage:
    def __init__(self, driver, timeout=15, retries=3, retry_delay=2):
        self.driver = driver
        self.timeout = timeout
        self.retries = retries
        self.retry_delay = retry_delay

    def find_element(self, by, value):
        for attempt in range(self.retries):
            try:
                return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located((by, value)))
            except Exception as err:
                if attempt < self.retries - 1:
                    time.sleep(self.retry_delay)
                else:
                    raise err

    def find_elements(self, by, value):
        for attempt in range(self.retries):
            try:
                return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_all_elements_located((by, value)))
            except Exception as err:
                if attempt < self.retries - 1:
                    time.sleep(self.retry_delay)
                else:
                    raise err