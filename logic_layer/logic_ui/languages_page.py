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
    SEARCH_BTN_XPAAH = '//input[contains(@class,"input text")]'
    PRESS_ON_SEARCH_BTN_XPATH = '//button[contains(@class,"submit-btn")]'
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

    # Method to click on langauges change page
    def click_on_languages(self):
        languages_button = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.LANGAUGES_BTN_XPATH)))
        languages_button.click()


    # Method to choose another language->we choose france
    def click_on_wanted_langauge(self):
        submit_button = WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable((By.XPATH,self.WANTED_LANGUAGE_XPATH )))
        submit_button.click()


    # a method navigate us to the search page
    def click_on_search_page(self):
        search_page = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.SEARCH_PAGE_XPATH)))
        search_page.click()


    # a method to click on the search bar and write something in france
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
        search_btn.click(

        )

    def click_on_home_btn(self):
        try:
            home_button = WebDriverWait(self._driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.LOGIN_BTN_XPATH)))
            home_button.click()
        except ElementClickInterceptedException:
            # Retry clicking on the menu
            home_button = WebDriverWait(self._driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.LOGIN_BTN_XPATH)))
            home_button.click()





    # Method to execute all steps of the change and check a new website language
    def execute_all_langauge_change_flow(self):
        try:
            self.click_on_languages()
            self.click_on_wanted_langauge()
            self.click_on_home_btn()
            return True
        except Exception as e:
            print(e)
            return False