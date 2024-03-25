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



    def __init__(self, num, list_info, cabs,areaName, driver=None):
        super().__init__(list_info)
        if driver is None:
            self.driver_set_up(cabs)
        else:
            self._driver = driver
        self.num = num
        self.list_info=list_info
        self.areaname=areaName



    # we click on our account page
    def click_on_account(self):
        try:
            my_account_button = WebDriverWait(self._driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.LOGIN_BTN_XPATH)))
            my_account_button.click()
        except ElementClickInterceptedException:
            # Retry clicking on the menu
            my_account_button = WebDriverWait(self._driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.LOGIN_BTN_XPATH)))
            my_account_button.click()



    # method to click on my areas and checks of turkey is in them-> return True , else ->return False
    def click_on_my_areas(self):
        area_componant = WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.GET_MY_AREAS)))
        result_text=area_componant.text
        if self.areaname[0] in result_text:
            return True
        else:
            return False





    # Method to execute all steps of the unsuccessful login process
    def execute_all_check_country_flow(self):
        try:
            # self.click_on_account()
            result=self.click_on_my_areas()
            return result
        except Exception as e:
            print(e)
            return False
