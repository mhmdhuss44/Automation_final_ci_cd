
class update_profile:

    def __init__(self,api_object,url):
        self.my_api = api_object
        self.url=url
        self.body={ "firstName": "mhmd",
                  "lastName": "huss",
                  "email": "mhmdhuss44@gmail.com",
                  "applicationData": {
                    "gfw": {
                      "country": "ISR",
                      "city": "haifa",
                      "sector": "Other",
                      "company": "there are no"
                    }
                  }
                }


    # change town name to another name
    def change_town_name(self):
        text_replace_url = f"{self.url}api/gfw/v2/user/65f96b22fb5b9d058a1ebca1/"
        response = self.my_api.api_patch_request(text_replace_url,self.body)
        return response







