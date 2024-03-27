import unittest
from Utilities import get_random_country_info, random_country_to_add
from infra_layer.infra_api.api_wrapper import APIWrapper
from logic_layer.logic_api.add_area_page import addArea


class AreaTests(unittest.TestCase):

    def setUp(self) -> None:
        self.my_api = APIWrapper()
        self.area_logic = addArea(self.my_api,self.my_api.url)


    # test to add an area to my areas list  - this is a completion to a ui test
    def test_add_new_area(self):
        # print("the chosen country is:",random_country_to_add)
        area_result = self.area_logic.add_new_area(random_country_to_add)
        self.assertEqual(area_result.status_code, 200, "Expected status code 200")







