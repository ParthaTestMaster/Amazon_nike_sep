import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from utilities.utils import Utils
from base.base_driver import BaseDriver



class homepage(BaseDriver):
    log = Utils.cutom_logger()
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    accept_cookies_button = "button[data-ref='cookie.accept-all']"
    departure_text_box_filed = "//input[@id='input-button__departure']"

    def accept_cookies(self):
        accept_button = self.wait_until_element_is_clickable(By.CSS_SELECTOR, self.accept_cookies_button)
        accept_button.click()

    def open_search_box(self,a,b):
        print(a)
        print(b)
        self.accept_cookies()
        self.wait_until_element_is_clickable(By.XPATH, self.departure_text_box_filed).click()
        time.sleep(5)
















