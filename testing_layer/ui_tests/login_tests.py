import concurrent.futures.thread
import time
import unittest
import concurrent.futures
from infra_layer.infra_ui.wrapper import browserWrapper
from logic_layer.logic_ui.login_page import loginLogic


class loginTests(unittest.TestCase):
    def setUp(self):
        self.infra_layer=browserWrapper()
        self.configs=self.infra_layer.get_all_configurations()


    def test_run_grid_serial(self):
        print(self.infra_layer.cab_list)
        for cabs in self.infra_layer.cab_list:
            self.test_verify_successful_add_to_cart(cabs)

    def test_run_grid_parallel(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.infra_layer.cab_list)) as executor:
            executor.map(self.test_verify_successful_add_to_cart, self.infra_layer.cab_list)


    # this ui_tests is to verify that we can successfuly login
    def test_verify_successful_add_to_cart(self, cab_info):
        cap, browser_type = cab_info

        self.loginPage = loginLogic(browser_type, self.infra_layer.get_all_configurations(), cap)
        self.loginPage.execute_all_log_in_flow()

        self.infra_layer.quit_drive(self.loginPage._driver)





