import concurrent.futures.thread
import time
import unittest
import concurrent.futures

from infra_layer.infra_ui.wrapper import browserWrapper
from logic_layer.logic_ui.check_country_page import checkCountryLogic
from logic_layer.logic_ui.login_page import loginLogic
from logic_layer.logic_ui.search_fail_page import searchfail
from logic_layer.logic_ui.search_sucess_page import searchSucess


class searchTests(unittest.TestCase):
    def setUp(self):
        self.infra_layer=browserWrapper()
        self.configs=self.infra_layer.get_all_configurations()


    def test_run_grid_serial(self):
        print(self.infra_layer.cab_list)
        for cabs in self.infra_layer.cab_list:
            self.test_verify_successful_area_add(cabs)

    def test_run_grid_parallel(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.infra_layer.cab_list)) as executor:
            executor.map(self.test_verify_successful_area_add, self.infra_layer.cab_list)


    # test_ui to verify that added an area successfully
    def test_verify_successful_area_add(self, cab_info):
        cap, browser_type = cab_info

        self.loginPage = loginLogic(browser_type, self.infra_layer.get_all_configurations(), cap)
        self.loginPage.execute_all_log_in_flow()

        self.added_area = checkCountryLogic(browser_type,self.infra_layer.get_all_configurations(),cap,self.loginPage._driver)
        result=self.added_area.execute_all_check_country_flow()
        assert result==True, "adding area has failed"

        self.infra_layer.quit_drive(self.added_area._driver)




























