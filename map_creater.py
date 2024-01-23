from pyecharts import options as opts
from pyecharts.charts import Map
from fake_useragent import UserAgent
from data_crawler import DataCrawler
class MapCreater:
    def __init__(self, file_url: str) -> None:
        crawler = DataCrawler(
            file_url,
            {
                "User-Agent": UserAgent().random
            }
        )
        #省份列表
        self.province_list = crawler.get_province_list()
        #人口列表
        self.population_list = crawler.get_population_list()
        #性别比列表
        self.gender_list = crawler.get_gender_list()
        #年龄构成表
        self.age_list = crawler.get_age_list()
        #受教育程度表
        self.education_list = crawler.get_education_list()
    #转换数据
    def get_data(self, province_list: list, other_list: list) -> list:
        list = []
        for i in range(0, len(other_list)):
            list.append((province_list[i], other_list[i]))
        return list
    #配置地图
    def get_map(self, title: str, data: list) -> Map:
        map = (
            Map(
                init_opts = opts.InitOpts(
                    width = "800px",
                    height = "600px"
                )
            )
            .add(
                series_name = title,
                data_pair = data,
                maptype = "china",
                zoom = 1.25,
                is_map_symbol_show = False
            )
            #全局配置项
            .set_global_opts(
                #设置标题
                # title_opts = opts.TitleOpts(title = title.split(" ")[0]),
                #设置标准显示
                visualmap_opts = opts.VisualMapOpts(
                    min_ = min([row[1] for row in data]),
                    max_ = max([row[1] for row in data]),
                    is_piecewise = False
                ),
            )
            #系列配置项
            .set_series_opts(
                label_opts = opts.LabelOpts(
                    is_show = True,
                    font_size = 8
                )
            )
        )
        return map
    def get_population_map_list(self) -> list:
        list = self.get_data(self.province_list, self.population_list)
        return [self.get_map("地区人口图 单位：人", list)]
    def get_gender_map_list(self) -> list:
        list1 = self.get_data(self.province_list, [row[0] for row in self.gender_list])
        list2 = self.get_data(self.province_list, [row[1] for row in self.gender_list])
        list3 = self.get_data(self.province_list, [row[2] for row in self.gender_list])
        return [
            self.get_map("男性人口性别构成图 单位：%", list1),
            self.get_map("女性人口性别构成图 单位：%", list2),
            self.get_map("人口性别比构成图 单位：%", list3)
        ]
    def get_age_map_list(self) -> list:
        list1 = self.get_data(self.province_list, [row[0] for row in self.age_list])
        list2 = self.get_data(self.province_list, [row[1] for row in self.age_list])
        list3 = self.get_data(self.province_list, [row[2] for row in self.age_list])
        list4 = self.get_data(self.province_list, [row[3] for row in self.age_list])
        return [
            self.get_map("0-14岁人口年龄构成图 单位：%", list1),
            self.get_map("14-59岁人口年龄构成图 单位：%", list2),
            self.get_map("60岁及以上人口年龄构成图 单位：%", list3),
            self.get_map("65岁及以上人口年龄构成图 单位：%", list4)
        ]
    def get_education_map_list(self) -> list:
        list1 = self.get_data(self.province_list, [row[0] for row in self.education_list])
        list2 = self.get_data(self.province_list, [row[1] for row in self.education_list])
        list3 = self.get_data(self.province_list, [row[2] for row in self.education_list])
        list4 = self.get_data(self.province_list, [row[3] for row in self.education_list])
        return [
            self.get_map("大学（大专及以上）受教育程度图 单位：人/10万人", list1),
            self.get_map("高中（含中专）受教育程度图 单位：人/10万人", list2),
            self.get_map("初中受教育程度图 单位：人/10万人", list3),
            self.get_map("小学受教育程度图 单位：人/10万人", list4)
        ]