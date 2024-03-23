import concurrent.futures.thread
import time
import unittest
import concurrent.futures

from infra_layer.infra_ui.wrapper import browserWrapper
from logic_layer.logic_ui.search_fail_page import searchfail
from logic_layer.logic_ui.search_overload import searchOverload
from logic_layer.logic_ui.search_sucess_page import searchSucess


class searchTests(unittest.TestCase):
    def setUp(self):
        self.infra_layer=browserWrapper()
        self.configs=self.infra_layer.get_all_configurations()


    def test_run_grid_serial(self):
        print(self.infra_layer.cab_list)
        for cabs in self.infra_layer.cab_list:
            self.test_verify_successful_overload_search(cabs)

    def test_run_grid_parallel(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.infra_layer.cab_list)) as executor:
            executor.map(self.test_verify_successful_overload_search, self.infra_layer.cab_list)


    # test_ui to verify that we can search in hebrw langaue
    def test_verify_successful_search(self, cab_info):
        cap, browser_type = cab_info

        self.search_success = searchSucess(browser_type,self.infra_layer.get_all_configurations(),cap)
        result=self.search_success.search_result_sucess_flow()
        assert result==True, "search has failed!"

        self.infra_layer.quit_drive(self.search_success._driver)


    # negative test_ui : test_ui to verify that when we search invalid input we dont get any serach result
    def test_verify_unsuccessful_search(self,cab_info):
        cap, browser_type = cab_info

        self.search_fail = searchfail(browser_type,self.infra_layer.get_all_configurations(),cap)
        result=self.search_fail.search_result_fail_flow()
        assert result==True, "searching invalid inputs has succeeded!"

        self.infra_layer.quit_drive(self.search_fail._driver)



    def test_verify_successful_overload_search(self, cab_info):
        cap, browser_type = cab_info

        self.search_success = searchOverload(browser_type,self.infra_layer.get_all_configurations(),cap)
        result=self.search_success.search_result_sucess_flow()
        assert result==True, "search overload has failed!"

        self.infra_layer.quit_drive(self.search_success._driver)

























