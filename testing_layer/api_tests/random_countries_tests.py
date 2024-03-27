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
        country_result,countryChosen = self.country_logic.get_random_country_info()
        print("The result:",country_result[0].json())
        try:
            self.assertEqual(country_result[0].status_code, 200, "Expected status code 200")
        except Exception as e:
            self.my_api.create_issue("failed get country info","Test to check count info has failed","KAN")
            self.fail("Test failed due to an exception: {}".format(str(e)))


    # test to check that the info we get belongs to the random country we choose
    def test_check_country_in_response(self):
        country_result,countryChosen = self.country_logic.get_random_country_info()
        print("The result:",country_result[0].json())
        try:
            self.assertIn(countryChosen, country_result[0].json(), "CountryChosen not found in response")
        except Exception as e:
            self.my_api.create_issue("failed to detected country in response","Test to check if the random country is in our response","KAN")
            self.fail("Test failed due to an exception: {}".format(str(e)))



    #  Test case to check if the areaHa attribute is a positive value
    def test_areaHa_positive(self):
        country_result, countryChosen = self.country_logic.get_random_country_info()
        areaHa = country_result[0].json()['data']['attributes']['areaHa']
        try:
            self.assertGreater(areaHa, 0, "AreaHa should be a positive value")
        except Exception as e:
            self.my_api.create_issue("areaha test has failed ","Test to check the areaha","KAN")
            self.fail("Test failed due to an exception: {}".format(str(e)))


    # Test case to check if the response contains the expected keys
    def test_response_keys(self):
        country_result, countryChosen = self.country_logic.get_random_country_info()
        expected_keys = ['type', 'id', 'attributes']
        response_keys = country_result[0].json()['data'].keys()
        self.assertCountEqual(expected_keys, response_keys, "Response keys mismatch")







