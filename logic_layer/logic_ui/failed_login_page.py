from selenium.common import NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra_layer.infra_ui.basePage import base

class loginFailLogic(base):
    LOGIN_BTN_XPATH='//a[@href="/my-gfw/"]'
    EMAIL_XPATH='//input[@name="email"]'
    PASSWORD_XPATH='//input[@name="password"]'
    SUBMIT_BTN_XPATH='//button[@class="c-button submit-btn"]'
    ERR_MESSAGE_XPATH='//div[@class="c-form-error"]'


    def __init__(self, num, list_info, cabs, driver=None):
        super().__init__(list_info)
        if driver is None:
            self.driver_set_up(cabs)
        else:
            self._driver = driver
        self.num = num
        self.list_info=list_info


    # Method to navigate us to the sign in page
    def click_on_sign_in(self):
        try:
            sign_in_button = WebDriverWait(self._driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.LOGIN_BTN_XPATH)))
            sign_in_button.click()
        except ElementClickInterceptedException:
            # Retry clicking on the menu
            sign_in_button = WebDriverWait(self._driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.LOGIN_BTN_XPATH)))
            sign_in_button.click()
        except StaleElementReferenceException:
            # Retry clicking on the menu
            sign_in_button = WebDriverWait(self._driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.LOGIN_BTN_XPATH)))
            sign_in_button.click()


    # method for entering an email adress
    def enter_email_adress(self):
        username_input = WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.EMAIL_XPATH)))
        username_input.send_keys(self.list_info["emailChrome"])


    # Method to enter a wrong password
    def enter_password(self, secret_pass):
        password_input = WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.PASSWORD_XPATH)))
        password_input.send_keys(secret_pass)


    # Method to click on the submit button
    def click_on_submit_btn(self):
        submit_button = WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable((By.XPATH,self.SUBMIT_BTN_XPATH )))
        submit_button.click()


    # Method to check if we get error message when we type wrong password->retrun True , else->return False
    def check_for_error_message(self):
        try:
            err_msg = WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable((By.XPATH,self.ERR_MESSAGE_XPATH )))
            return True
        except Exception as e:
            print(e)
            return False




    # Method to execute all steps of the unsuccessful login process
    def execute_all_failed_log_in_flow(self):
        try:
            self.click_on_sign_in()
            self.enter_email_adress()
            self.enter_password("123456789")
            self.click_on_submit_btn()
            result=self.check_for_error_message()
            return result
        except Exception as e:
            print(e)
            return False