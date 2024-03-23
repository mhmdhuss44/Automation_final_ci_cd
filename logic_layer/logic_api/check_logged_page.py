
class check_logged:

    def __init__(self,api_object,url):
        self.my_api = api_object
        self.url=url


    # here we do an api check to see if we are logged in - we should get our login details
    def checked_logged_in(self):
        text_replace_url = f"https://api.resourcewatch.org/auth/check-logged"
        response = self.my_api.api_get_request(text_replace_url)
        return response







