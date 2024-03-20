import concurrent.futures.thread
import time
import unittest
import concurrent.futures
from infra_layer.infra_ui.wrapper import browserWrapper
from logic_layer.logic_ui.failed_login_page import loginFailLogic
from logic_layer.logic_ui.login_page import loginLogic
from logic_layer.logic_ui.logout_page import logoutLogic


class loginTests(unittest.TestCase):
    def setUp(self):
        self.infra_layer=browserWrapper()
        self.configs=self.infra_layer.get_all_configurations()


    def test_run_grid_serial(self):
        print(self.infra_layer.cab_list)
        for cabs in self.infra_layer.cab_list:
            self.test_verify_successful_log_in(cabs)

    def test_run_grid_parallel(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.infra_layer.cab_list)) as executor:
            executor.map(self.test_verify_successful_log_in, self.infra_layer.cab_list)


    # this ui_tests is to verify that we can successfuly login
    def test_verify_successful_log_in(self, cab_info):
        cap, browser_type = cab_info

        self.loginPage = loginLogic(browser_type, self.infra_layer.get_all_configurations(), cap)
        result=self.loginPage.execute_all_log_in_flow()

        assert result == True, "The logout Process has failed"
        self.infra_layer.quit_drive(self.loginPage._driver)


    def test_verify_successful_log_out(self, cab_info):
        cap, browser_type = cab_info

        self.loginPage = loginLogic(browser_type, self.infra_layer.get_all_configurations(), cap)
        self.loginPage.execute_all_log_in_flow()

        self.logoutPage = logoutLogic(browser_type, self.infra_layer.get_all_configurations(), cap,self.loginPage._driver)
        result=self.logoutPage.execute_all_log_out_flow()

        assert result==True,"The logout Process has failed"
        self.infra_layer.quit_drive(self.logoutPage._driver)



    def test_verify_unsuccessful_log_in(self, cab_info):
        cap, browser_type = cab_info

        self.loginPage = loginLogic(browser_type, self.infra_layer.get_all_configurations(), cap)
        self.loginPage.execute_all_log_in_flow()

        self.failedLogin = loginFailLogic(browser_type, self.infra_layer.get_all_configurations(), cap,self.loginPage._driver)
        result=self.failedLogin.execute_all_failed_log_in_flow()

        assert result==True,"Error! success in login with wrong info!"
        self.infra_layer.quit_drive(self.logoutPage._driver)





