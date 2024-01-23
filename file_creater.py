from pyecharts import options as opts
from pyecharts.charts import Page
from map_creater import MapCreater
class FileCreater:
    #解析网址
    def set_file_url(self, file_url: str) -> None:
        self.file_url = file_url
    #保存路径
    def set_dir_name(self, dir_name: str) -> None:
        self.dir_name = dir_name
    #生成地图
    def get_map_file(self, id_list: list) -> None:
        creater = MapCreater(self.file_url)
        map_list = [
            creater.get_population_map_list(),
            creater.get_gender_map_list(),
            creater.get_age_map_list(),
            creater.get_education_map_list()
        ]
        map_name_dict = {
            1: "population",
            2: "gender",
            3: "age",
            4: "education"
        }
        for i in range(0, len(id_list)):
            if id_list[i] == 0:
                continue
            page = Page(
                page_title = "map_{}".format(map_name_dict[i + 1]),
                layout = opts.PageLayoutOpts(
                    justify_content = "center",
                    display = "flex",
                    flex_wrap = "wrap"
                )
            )
            for j in range(0, len(map_list[i])):
                page.add(map_list[i][j])
            if hasattr(self, "dir_name") == False:
                self.set_dir_name(".")
            page.render("{}/map_{}.html".format(self.dir_name, map_name_dict[i + 1]))