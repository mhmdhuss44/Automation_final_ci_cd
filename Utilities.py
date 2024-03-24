import random2

def get_random_town():
    israel_towns = [
        "Jerusalem", "Tel Aviv", "Haifa", "Rishon LeZion",
        "Petah Tikva","Ashdod","Netanya","Beer Sheva","Holon",
        "Bnei Brak","Ramat Gan","Ashkelon","Bat Yam","Herzliya",
        "Kfar Saba","Hadera","Ra'anana","Ramat HaSharon","Nahariya", "Lod",
        "Rosh HaAyin","Beitar Illit","Qiryat Ata",
        "Acre","Eilat","Nahariya","Tiberias", "Safed","Kiryat Gat",
        "Nazareth","Umm al-Fahm","Sakhnin","Tayibe","Kafr Qasim","Tamra","Kfar Qara",
        "Shfaram","Arraba","Bu'eine Nujeidat","Fureidis","Ar'ara","Kafr Kanna",
        "Iksal","Tira","Jisr az-Zarqa","Jatt","Deir al-Asad","Maghar",
        "Yafa an-Naseriyye","Kafr Manda","Deir Hanna","Kafr Bara","Ein Mahel",
        "Tuba-Zangariyye","Kabul","Beit Jann","Musmus","Daburiyya",
        "Basmat Tab'un","Al-Mashhad","Majd al-Krum",
        "Shibli–Umm al-Ghanam","Kafr Yasif","Kafr Misr","Bir al-Maksur",
    ]
    return random2.choice(israel_towns)


def get_random_country_info():
    countries = [
        ("France", "FRA", "a38805b977bec78f38c05dbb77c469fc"),
        ("Italy", "ITA", "d254ee97893949396330c9f9df5c9f07"),
        ("Spain", "ESP", "178b7111927200e6bcef00175f934762"),
        ("Israel", "ISR", "67bbcb19cb9450588378e8f8d426b594"),
        ("Turkey", "TUR", "25b7154c624e134d1a4d75a0ae8ae978"),
        ("Germany", "DEU", "e7079f33079e6b06fd008258cca8d22b"),
        ("Greece", "GRC", "0b900ade3cd2c58cacc2ec04f00ec0a3"),
        ("Poland","POL","237be02414ff1f1f32fa2a7ede474c8f"),
        ("Japan", "JPN", "67c12479fc787b0bf88e1d7d08825d97"),
        ("China", "CHN", "d59a43df7b0a643bfe72c11fd0060199"),
        ("India", "IND", "45d0f6f887a18df373fa69c3eb6f13c7")]

    return random2.choice(countries)


