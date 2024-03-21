# Class to handle another ui_tests, ensuring that we can't login with the wrong password
import time
from selenium.common import NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra_layer.infra_ui.basePage import base

class checkCountryLogic(base):
    LOGIN_BTN_XPATH='//a[@href="/my-gfw/"]'
    GET_MY_AREAS='//div[@class="item-body"]'



    def __init__(self, num, list_info, cabs, driver=None):
        super().__init__(list_info)
        if driver is None:
            self.driver_set_up(cabs)
        else:
            self._driver = driver
        self.num = num
        self.list_info=list_info

    # Method on sign in
    def click_on_account(self):
        try:
            button = WebDriverWait(self._driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.LOGIN_BTN_XPATH)))
            button.click()
        except ElementClickInterceptedException:
            # Retry clicking on the menu
            button = WebDriverWait(self._driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.LOGIN_BTN_XPATH)))
            button.click()
        except StaleElementReferenceException:
            # Retry clicking on the menu
            button = WebDriverWait(self._driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.LOGIN_BTN_XPATH)))
            button.click()


    # method to click on the logout button
    def click_on_my_areas(self):
        area_componant = WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.GET_MY_AREAS)))
        result_text=area_componant.text
        if "Turkey" in result_text:
            return True
        else:
            return False





    # Method to execute all steps of the unsuccessful login process
    def execute_all_check_country_flow(self):
        self.click_on_account()
        time.sleep(2)
        result=self.click_on_my_areas()
        time.sleep(5)
        return result
