import unittest
from infra_layer.infra_api.api_wrapper import APIWrapper
from logic_layer.logic_api.add_area_page import addArea
from logic_layer.logic_api.update_profile_page import update_profile


class AreaTests(unittest.TestCase):

    def setUp(self) -> None:
        self.my_api = APIWrapper()
        self.area_logic = addArea(self.my_api,self.my_api.url)


    # to make sure that we chnaged the town successfully - this is a completion to a ui test
    def test_add_new_area(self):
        # first variable is the wanted password len , third is for conating any digit, third for upper case letter and fourth for special char
        area_result = self.area_logic.add_new_area()
        print("The result:",area_result.json())
        self.assertEqual(area_result.status_code, 200, "Expected status code 200")







