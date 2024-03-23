import unittest
from infra_layer.infra_api.api_wrapper import APIWrapper
from logic_layer.logic_api.update_profile_page import update_profile


class profileTests(unittest.TestCase):

    def setUp(self) -> None:
        self.my_api = APIWrapper()
        self.profile_logic = update_profile(self.my_api,self.my_api.url)


    # to make sure that we chnaged the town successfully
    def test_update_town_in_profile(self):
        town_mod_result = self.profile_logic.change_town_name()
        print("The result:",town_mod_result.json())
        self.assertEqual(town_mod_result.status_code, 200, "Expected status code 200")



    # test to check that we have the new town name in profile (haifa town)
    def test_check_town_in_profile(self):
        town_mod_result = self.profile_logic.change_town_name()
        city = town_mod_result.json()['data']['attributes']['applicationData']['gfw']['city']
        if city.lower() == 'haifa':
            result=True
        else:
            result=False
        assert  result==True , "town wasnt changed to haifa..."







