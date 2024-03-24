import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra_layer.infra_ui.basePage import base


class searchfail(base):
    SEARCH_PAGE_XPATH = '//a[@href="/search/"]'
    SEARCH_BTN_XPAAH = '//input[contains(@class,"input text")]'
    PRESS_ON_SEARCH_BTN_XPATH = '//button[contains(@class,"submit-btn")]'
    FIRST_SEARCH_RESULT = '//div[@class="search-item"]'
    NO_RESULTS_XPATH='//div[@class="no-results"]'


    def __init__(self, num, list_info, cabs, driver=None):
        super().__init__(list_info)
        if driver is None:
            self.driver_set_up(cabs)
        else:
            self._driver = driver
        self.num = num

    # a method navigate us to the search page
    def click_on_search_page(self):
        search_page = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.SEARCH_PAGE_XPATH)))
        search_page.click()

    # a method to click on the search bar and write something
    def click_on_search_bar_and_type(self):
        search_bar = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.SEARCH_BTN_XPAAH)))
        search_bar.click()
        search_bar.clear()  # Clear any existing text in the input field
        search_bar.send_keys("#$#")

    # a method to click on the search
    def click_on_search_btn(self):
        search_btn = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.PRESS_ON_SEARCH_BTN_XPATH)))
        search_btn.click()



    # takes the first result and checks if its relevant
    def check_on_error_result(self):
        try:
            result = WebDriverWait(self._driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.NO_RESULTS_XPATH)))
            return True
        except Exception as e:
            print(e)
            return False



    def search_result_fail_flow(self):
        try:
            self.click_on_search_page()
            self.click_on_search_bar_and_type()
            self.click_on_search_btn()
            result = self.check_on_error_result()
            return result
        except Exception as e:
            print(e)
            return False





