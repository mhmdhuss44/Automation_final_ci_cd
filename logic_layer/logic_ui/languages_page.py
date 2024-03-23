# Class to handle another ui_tests, ensuring that we can't login with the wrong password
import time
from selenium.common import NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra_layer.infra_ui.basePage import base

class languageLogic(base):
    LANGAUGES_BTN_XPATH='//button[@aria-label="English"]'
    WANTED_LANGUAGE_XPATH='//button[text()="Français"]'
    SEARCH_PAGE_XPATH = '//a[@href="/search/"]'
    SEARCH_BTN_XPAAH = '//input[@class="input text css-195ifoz efi91wg0"]'
    PRESS_ON_SEARCH_BTN_XPATH = '//button[@class="submit-btn css-141bgb3 eda4b3r0"]'
    FIRST_SEARCH_RESULT = '//div[@class="search-item"]'
    LOGIN_BTN_XPATH = '//a[@href="/my-gfw/"]'


    def __init__(self, num, list_info, cabs, driver=None):
        super().__init__(list_info)
        if driver is None:
            self.driver_set_up(cabs)
        else:
            self._driver = driver
        self.num = num
        self.list_info=list_info

    # Method to click on langauges
    def click_on_languages(self):
        try:
            button = WebDriverWait(self._driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.LANGAUGES_BTN_XPATH)))
            button.click()
        except ElementClickInterceptedException:
            # Retry clicking on the menu
            button = WebDriverWait(self._driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.LANGAUGES_BTN_XPATH)))
            button.click()
        except StaleElementReferenceException:
            # Retry clicking on the menu
            button = WebDriverWait(self._driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.LANGAUGES_BTN_XPATH)))
            button.click()



    # Method to click on the submit button
    def click_on_wanted_langauge(self):
        submit_button = WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable((By.XPATH,self.WANTED_LANGUAGE_XPATH )))
        submit_button.click()

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
        search_bar.send_keys("arbre")

        # a method to click on the search

    def click_on_search_btn(self):
        search_btn = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.PRESS_ON_SEARCH_BTN_XPATH)))
        search_btn.click()

    def click_on_home_btn(self):
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



        # takes the first result and checks if its relevant

    def check_on_first_result(self):
        first_result = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.FIRST_SEARCH_RESULT)))
        name_of_result = first_result.text
        if "forest" in name_of_result:
            return True
        else:
            return False

    # Method to execute all steps of the unsuccessful login process
    def execute_all_langauge_change_flow(self):
        try:
            self.click_on_languages()
            time.sleep(2)
            self.click_on_wanted_langauge()
            time.sleep(1)
            self.click_on_home_btn()
            time.sleep(2)
            # self.click_on_search_page()
            # self.click_on_search_bar_and_type()
            # self.click_on_search_btn()
            # result = self.check_on_first_result()
            return True
        except Exception as e:
            print(e)
            return False