import concurrent.futures.thread
import time
import unittest
import concurrent.futures
from infra_layer.infra_ui.wrapper import browserWrapper
from logic_layer.logic_ui.login_page import loginLogic
from logic_layer.logic_ui.profile_info_page import profileInfoLogic


class profileChangeTests(unittest.TestCase):
    def setUp(self):
        self.infra_layer=browserWrapper()
        self.configs=self.infra_layer.get_all_configurations()

    def tearDown(self) -> None:
        self.infra_layer.quit_drive(self.result_driver)



    def test_run_grid_serial(self):
        print(self.infra_layer.cab_list)
        for cabs in self.infra_layer.cab_list:
            self.test_verify_successful_town_change(cabs)

    def test_run_grid_parallel(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.infra_layer.cab_list)) as executor:
            executor.map(self.test_verify_successful_town_change, self.infra_layer.cab_list)


    # test to verify that the new town name is changed - this is connected to a test in the api tests
    def test_verify_successful_town_change(self, cab_info):
        cap, browser_type = cab_info

        self.loginPage = loginLogic(browser_type, self.infra_layer.get_all_configurations(), cap)
        self.loginPage.execute_all_log_in_flow()

        self.modify_profile_Page=profileInfoLogic(browser_type, self.infra_layer.get_all_configurations(), cap,self.loginPage._driver)
        result=self.modify_profile_Page.execute_all_profile_change_flow()
        self.result_driver=self.modify_profile_Page._driver

        assert result == "haifa", "changing location has failed"










