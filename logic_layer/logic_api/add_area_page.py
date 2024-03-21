
class addArea:

    def __init__(self,api_object,url):
        self.my_api = api_object
        self.url=url
        self.body={
                    "id": None,
                    "name": "Turkey",
                    "type": "country",
                    "application": "gfw",
                    "geostore": "25b7154c624e134d1a4d75a0ae8ae978",
                    "email": "mhmdhuss44@gmail.com",
                    "language": "en",
                    "deforestationAlerts": False,
                    "deforestationAlertsType": "glad-all",
                    "monthlySummary": False,
                    "fireAlerts": False,
                    "admin": {
                        "adm0": "TUR"
                    },
                    "tags": [],
                    "public": False,
                    "status": "saved"
                }


    # change town name to another name
    def add_new_area(self):
        area_url = f"{self.url}api/gfw/v2/area/"
        response = self.my_api.api_post_request(area_url,self.body)
        return response








