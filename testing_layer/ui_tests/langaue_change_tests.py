import concurrent.futures.thread
import time
import unittest
import concurrent.futures
from infra_layer.infra_ui.wrapper import browserWrapper
from logic_layer.logic_ui.languages_page import languageLogic
from logic_layer.logic_ui.login_page import loginLogic
from logic_layer.logic_ui.search_sucess_page import searchSucess

# aa
class languageTests(unittest.TestCase):
    def setUp(self):
        self.infra_layer=browserWrapper()
        self.configs=self.infra_layer.get_all_configurations()


    def tearDown(self) -> None:
        self.infra_layer.quit_drive(self.result_driver)


    def test_run_grid_serial(self):
        print(self.infra_layer.cab_list)
        for cabs in self.infra_layer.cab_list:
            self.test_verify_successful_login_different_langauge(cabs)

    def test_run_grid_parallel(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.infra_layer.cab_list)) as executor:
            executor.map(self.test_verify_successful_login_different_langauge, self.infra_layer.cab_list)


    # test_ui to verify that we can search under different language settings
    def test_verify_successful_search_different_langauge(self, cab_info):
        cap, browser_type = cab_info


        self.search_language = languageLogic(browser_type, self.infra_layer.get_all_configurations(), cap)
        changing_language_result = self.search_language.execute_all_langauge_change_flow()

        self.search_success = searchSucess(browser_type,self.infra_layer.get_all_configurations(),cap,self.search_language._driver)
        result=self.search_success.search_result_sucess_flow()
        self.result_driver=self.search_success._driver

        assert result==True, "search has failed!"



    # ui test to verify that we can successfuly login when changing our account language
    def test_verify_successful_login_different_langauge(self, cab_info):
        cap, browser_type = cab_info


        self.langauge_change = languageLogic(browser_type, self.infra_layer.get_all_configurations(), cap)
        changing_language_result = self.langauge_change.execute_all_langauge_change_flow()

        self.loginPage = loginLogic(browser_type, self.infra_layer.get_all_configurations(), cap,self.langauge_change._driver)
        result = self.loginPage.execute_all_log_in_flow()
        self.result_driver=self.loginPage._driver

        assert result == True, "The logout Process has failed"






























