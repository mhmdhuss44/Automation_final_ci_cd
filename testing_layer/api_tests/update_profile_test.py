import unittest
from infra_layer.infra_api.api_wrapper import APIWrapper
from logic_layer.logic_api.update_profile_page import update_profile


class passwordTests(unittest.TestCase):

    def setUp(self) -> None:
        self.my_api = APIWrapper()
        self.password_logic = update_profile(self.my_api,self.my_api.url)


    # to make sure that we chnaged the town successfully
    def test_update_town_in_profile(self):
        # first variable is the wanted password len , third is for conating any digit, third for upper case letter and fourth for special char
        town_mod_result = self.password_logic.change_town_name()
        print("The result:",town_mod_result.json())
        self.assertEqual(town_mod_result.status_code, 200, "Expected status code 200")




