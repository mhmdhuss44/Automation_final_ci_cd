import time
from selenium.common import NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra_layer.infra_ui.basePage import base

class profileInfoLogic(base):

    USR_PROFILE_XPATH='//a[@href="/my-gfw/"]'
    UPDATE_PROFILE_BTN_XPATH='//button[@class="user-btn css-6lid9l eda4b3r0"]'
    CURNT_TOWN_XPATH="//input[@class='c-form-input' and @name='city']"


    def __init__(self, num, list_info, cabs, driver=None):
        super().__init__(list_info)
        if driver is None:
            self.driver_set_up(cabs)
        else:
            self._driver = driver
        self.num = num
        self.list_info=list_info

    # Method on click on user page
    def click_on_sign_in(self):
        try:
            user_page_button = WebDriverWait(self._driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.USR_PROFILE_XPATH)))
            user_page_button.click()
        except ElementClickInterceptedException:
            # Retry clicking on the menu
            user_page_button = WebDriverWait(self._driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.USR_PROFILE_XPATH)))
            user_page_button.click()
        except StaleElementReferenceException:
            # Retry clicking on the menu
            user_page_button = WebDriverWait(self._driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.USR_PROFILE_XPATH)))
            user_page_button.click()


    # Method to click on the update profile button
    def click_on_update_prof(self):
        update_profile_button = WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.UPDATE_PROFILE_BTN_XPATH)))
        update_profile_button.click()


    # Method to get the towns info and return it
    def get_town_info(self):
        button = WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH,self.CURNT_TOWN_XPATH )))
        city_value = button.get_attribute("value")
        print(city_value)
        return city_value



    # Method to execute all steps of the get town  process
    def execute_all_profile_change_flow(self):
        self.click_on_update_prof()
        result=self.get_town_info()
        return result
