import random2


class countryInfo:

    def __init__(self,api_object,url):
        self.my_api = api_object
        self.url=url

    def random_country(self):
        country_iso = [
            "USA", "CHN", "JPN", "DEU", "GBR", "FRA", "ITA", "CAN", "RUS", "IND", "BRA", "AUS", "ESP", "NLD", "CHE",
            "SWE", "KOR", "BEL", "TUR", "ISR", "SGP", "NZL", "ARE", "MEX", "ARG", "POL", "IDN", "SAU", "THA", "ZAF",
            "EGY", "NGA", "PAK", "COL", "IRN", "VNM", "BGD", "UKR", "MYS", "PHL", "NOR", "PER", "FIN", "VEN", "CHL",
            "ROU", "CZE", "HUN", "AUT", "GRC", "PRT", "DNK", "IRL", "KAZ", "KEN", "NGA", "MYS", "PAK", "NOR", "SAU",
            "ZAF", "SWE", "CHE", "TUR", "ARE", "UKR", "ZAF", "DZA", "ARG", "AUT", "BHR", "BGD", "BLR", "BOL", "BGR",
            "CMR", "CRI", "HRV", "CUB", "CYP", "DNK", "ECU", "EST", "ETH", "FIN", "GEO", "GHA", "GTM", "HKG", "ISL",
            "JOR", "KWT", "LVA", "LTU", "LUX", "MLT", "MAR", "NGA", "OMN", "PAN", "PRY", "PER", "PHL", "QAT", "SRB",
            "SVK", "SVN", "LKA", "SDN", "TZA", "TTO", "TUN", "UGA", "URY", "UZB", "VEN", "VNM", "YEM", "ZMB", "ZWE"
        ]

        return random2.choice(country_iso)



    # change town name to another name
    def get_random_country_info(self):
        rand_country=self.random_country()
        country_url = f"{self.url}api/gfw/v2/geostore/admin/{rand_country}/?thresh=0.005"
        response = self.my_api.api_get_request(country_url)
        return response









