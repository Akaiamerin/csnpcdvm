import requests
from bs4 import BeautifulSoup
class DataCrawler:
    def __init__(self, url: str, headers: map) -> None:
        req = requests.get(
            url = url,
            headers = headers
        )
        self.soup = BeautifulSoup(req.text, "lxml")
        self.tbody = self.soup.select("tbody")
    #省份列表
    def get_province_list(self) -> list:
        list = []
        tr_list = self.tbody[0].select("tr")
        for i in range(3, len(tr_list) - 1):
            province_name = tr_list[i].select("span")[0].text
            #省份全称
            if province_name in ["北京", "天津", "上海", "重庆"]:
                province_name = province_name + "市"
            elif province_name in ["内蒙古","西藏"]:
                province_name = province_name + "自治区"
            elif province_name == "广西":
                province_name = "广西壮族自治区"
            elif province_name == "新疆":
                province_name = "新疆维吾尔自治区"
            elif province_name == "宁夏":
                province_name = "宁夏回族自治区"
            elif province_name in ["香港","澳门"]:
                province_name = province_name + "特别行政区"
            else:
                province_name = province_name + "省"
            list.append(province_name)
        list.append("香港特别行政区")
        list.append("澳门特别行政区")
        list.append("台湾省")
        return list
    #人口列表
    def get_population_list(self) -> list:
        list = []
        tr_list = self.tbody[0].select("tr")
        for i in range(3, len(tr_list) - 1):
            list.append(int(tr_list[i].select("span")[1].text))
        list.append(int(self.soup.select("div[data-uuid = \"sx49DpYAczML\"] span")[2].text[1: -2])) #港
        list.append(int(self.soup.select("div[data-uuid = \"sx49DpZ3ZQJy\"] span")[2].text[1: -2])) #澳
        list.append(int(self.soup.select("div[data-uuid = \"sx49DpZXUnzU\"] span")[2].text[1: -2])) #台
        return list
    #性别比列表
    def get_gender_list(self) -> list:
        list = []
        tr_list = self.tbody[1].select("tr")
        for i in range(3, len(tr_list)):
            text1 = float(tr_list[i].select("span")[1].text) #男性比例
            text2 = float(tr_list[i].select("span")[2].text) #女性比例
            text3 = float(tr_list[i].select("span")[3].text) #性别比
            list.append([text1, text2, text3])
        return list
    #年龄构成表
    def get_age_list(self) -> list:
        list = []
        tr_list = self.tbody[3].select("tr")
        for i in range(4, len(tr_list)):
            text1 = float(tr_list[i].select("div")[1].select("span")[0].text) #0-14
            text2 = float(tr_list[i].select("div")[2].select("span")[0].text) #14-59
            text3 = float(tr_list[i].select("div")[3].select("span")[0].text) #60
            text4 = float(tr_list[i].select("div")[4].select("span")[0].text) #65
            list.append([text1, text2, text3, text4])
        return list
    #受教育程度表
    def get_education_list(self) -> list:
        list = []
        tr_list = self.tbody[4].select("tr")
        for i in range(3, len(tr_list)):
            text1 = int(tr_list[i].select("div")[1].select("span")[0].text) #大学（大专及以上）
            text2 = int(tr_list[i].select("div")[2].select("span")[0].text) #高中（含中专）
            text3 = int(tr_list[i].select("div")[3].select("span")[0].text) #初中
            text4 = int(tr_list[i].select("div")[4].select("span")[0].text) #小学
            list.append([text1, text2, text3, text4])
        return list