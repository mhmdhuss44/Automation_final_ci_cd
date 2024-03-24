import unittest
from infra_layer.infra_api.api_wrapper import APIWrapper
from logic_layer.logic_api.check_logged_page import check_logged


class loggedInfoTests(unittest.TestCase):

    def setUp(self) -> None:
        self.my_api = APIWrapper()
        self.login_logic = check_logged(self.my_api,self.my_api.url)
        self.login_result = self.login_logic.get_login_details()



    # to make sure that we suceesfully are logged in with valid details
    def test_check_if_success_logged_in(self):
        print("The result:",self.login_result.json())
        self.assertEqual(self.login_result.status_code, 200, "Expected status code 200")


    # Test if the ID matches the expected ID (thats written in the json file)
    def test_check_id(self):
        response_data = self.login_result.json()
        self.assertEqual(response_data["id"], self.my_api.usr_id, "ID does not match")


    # Test if the email matches the expected email (thats written in the json file)
    def test_check_email(self):
        response_data = self.login_result.json()
        self.assertEqual(response_data["email"], self.my_api.emailAdress, "Email does not match")











