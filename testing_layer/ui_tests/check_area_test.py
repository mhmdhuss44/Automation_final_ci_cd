import concurrent.futures.thread
import time
import unittest
import concurrent.futures
from infra_layer.infra_ui.wrapper import browserWrapper
from logic_layer.logic_ui.check_country_page import checkCountryLogic
from logic_layer.logic_ui.login_page import loginLogic



class areaTests(unittest.TestCase):
    def setUp(self):
        self.infra_layer=browserWrapper()
        self.configs=self.infra_layer.get_all_configurations()


    # test_ui to verify that added an area successfully - this is a completion of an api test
    def verify_successful_area_add(self, cab_info,infra_layer):
        cap, browser_type = cab_info

        self.loginPage = loginLogic(browser_type, infra_layer.get_all_configurations(), cap)
        self.loginPage.execute_all_log_in_flow()

        self.added_area = checkCountryLogic(browser_type,infra_layer.get_all_configurations(),cap,self.loginPage._driver)
        result=self.added_area.execute_all_check_country_flow()
        assert result==True, "adding area has failed"

        infra_layer.quit_drive(self.added_area._driver)




























