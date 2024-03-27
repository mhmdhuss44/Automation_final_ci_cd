import time
from selenium.common import NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra_layer.infra_ui.basePage import base

class logoutLogic(base):
    LOGIN_BTN_XPATH='//a[@href="/my-gfw/"]'
    LOGOUT_BTN_XPATH='//button[@fdprocessedid="s11e3a"]'
    PASSWORD_XPATH = '//input[@name="password"]'


    def __init__(self, num, list_info, cabs, driver=None):
        super().__init__(list_info)
        if driver is None:
            self.driver_set_up(cabs)
        else:
            self._driver = driver
        self.num = num
        self.list_info=list_info

    # Method on navigate to the login info page
    def click_on_sign_in(self):
        try:
            login_home_page = WebDriverWait(self._driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.LOGIN_BTN_XPATH)))
            login_home_page.click()
        except ElementClickInterceptedException:
            # Retry clicking on the menu
            login_home_page = WebDriverWait(self._driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.LOGIN_BTN_XPATH)))
            login_home_page.click()
        except StaleElementReferenceException:
            # Retry clicking on the menu
            login_home_page = WebDriverWait(self._driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.LOGIN_BTN_XPATH)))
            login_home_page.click()


    # method to click on the logout button
    def click_on_logout_btn(self):
        logout_button = WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.LOGOUT_BTN_XPATH)))
        logout_button.click()


    # method to verify that the logout is successful by checking elemnts on the page
    def verify_success_logout(self):
        try:
            password_input = WebDriverWait(self._driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.PASSWORD_XPATH)))
            return True
        except Exception as e:
            return False





    # Method to execute all steps of the unsuccessful login process
    def execute_all_log_out_flow(self):
        self.click_on_logout_btn()
        result=self.verify_success_logout()
        return result