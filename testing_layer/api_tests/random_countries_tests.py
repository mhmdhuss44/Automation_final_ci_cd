import unittest
from infra_layer.infra_api.api_wrapper import APIWrapper
from logic_layer.logic_api.add_area_page import addArea
from logic_layer.logic_api.country_info_page import countryInfo


class countriesTests(unittest.TestCase):

    def setUp(self) -> None:
        self.my_api = APIWrapper()
        self.country_logic = countryInfo(self.my_api,self.my_api.url)


    # we get a random country and then its info
    def test_get_country_info(self):
        country_result = self.country_logic.get_random_country_info()
        print("The result:",country_result.json())
        self.assertEqual(country_result.status_code, 200, "Expected status code 200")







