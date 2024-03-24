
class addArea:

    def __init__(self,api_object,url):
        self.my_api = api_object
        self.url=url



    # method to create the wanted area body
    def create_area_body(self,random_country_to_add):
        self.body = {
            "id": None,
            "name": random_country_to_add[0],
            "type": "country",
            "application": "gfw",
            "geostore": random_country_to_add[2],
            "email": "mhmdhuss44@gmail.com",
            "language": "en",
            "deforestationAlerts": False,
            "deforestationAlertsType": "glad-all",
            "monthlySummary": False,
            "fireAlerts": False,
            "admin": {
                "adm0": random_country_to_add[1]
            },
            "tags": [],
            "public": False,
            "status": "saved"
        }



    # method to add a new area to my areas
    def add_new_area(self,random_country_to_add):
        self.create_area_body(random_country_to_add)
        area_url = f"{self.url}api/gfw/v2/area/"
        response = self.my_api.api_post_request(area_url,self.body)
        return response








