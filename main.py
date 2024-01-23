from tkinter import Tk
from tkinter import Label
from tkinter import Frame
from tkinter import IntVar
from tkinter import Checkbutton
from tkinter import Button
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showerror
from tkinter.messagebox import askyesno
import os
import webbrowser
from file_creater import FileCreater
def init(url: str) -> None:
    creater = FileCreater()
    root = Tk()
    title = "中国第七次全国人口普查数据可视化地图"
    root.title(title)
    #居中
    width = 800
    height = 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = int(screen_width / 2 - width / 2)
    y = int(screen_height / 2 - height / 2)
    root.geometry("{}x{}+{}+{}".format(width, height, x, y))
    #标题
    label1 = Label(
        master = root,
        fg = "#333333",
        font = ("微软雅黑", 24),
        text = title
    )
    label1.pack(
        anchor = "center",
        ipadx = width,
        ipady = height / 10
    )
    frame1 = Frame(master = root)
    frame1.pack()
    frame11 = Frame(master = frame1)
    #全选
    select_all_var = IntVar()
    select_all_check_btn = Checkbutton(
        master = frame11,
        font = ("微软雅黑", 18),
        text = "全选",
        offvalue = 0,
        onvalue = 1,
        variable = select_all_var
    )
    select_all_check_btn.pack(side = "left")
    def set_select_all(event) -> None:
        if select_all_var.get() == 0:
            check_btn1.select()
            check_btn2.select()
            check_btn3.select()
            check_btn4.select()
        else:
            check_btn1.deselect()
            check_btn2.deselect()
            check_btn3.deselect()
            check_btn4.deselect()
    select_all_check_btn.bind(
        sequence = "<Button-1>",
        func = set_select_all
    )
    frame11.pack()
    frame12 = Frame(master = frame1)
    #地区人口图
    check_btn1_var = IntVar()
    check_btn1 = Checkbutton(
        master = frame12,
        font = ("微软雅黑", 18),
        text = "地区人口图",
        offvalue = 0,
        onvalue = 1,
        variable = check_btn1_var
    )
    #人口性别比构成图
    check_btn2_var = IntVar()
    check_btn2 = Checkbutton(
        master = frame12,
        font = ("微软雅黑", 18),
        text = "人口性别比构成图",
        offvalue = 0,
        onvalue = 1,
        variable = check_btn2_var
    )
    #人口年龄构成图
    check_btn3_var = IntVar()
    check_btn3 = Checkbutton(
        master = frame12,
        font = ("微软雅黑", 18),
        text = "人口年龄构成图",
        offvalue = 0,
        onvalue = 1,
        variable = check_btn3_var
    )
    #受教育程度图
    check_btn4_var = IntVar()
    check_btn4 = Checkbutton(
        master = frame12,
        font = ("微软雅黑", 18),
        text = "受教育程度图",
        offvalue = 0,
        onvalue = 1,
        variable = check_btn4_var
    )
    check_btn1.pack(side = "left")
    check_btn2.pack(side = "left")
    check_btn3.pack(side = "left")
    check_btn4.pack(side = "left")
    frame12.pack(ipady = 20)
    frame13 = Frame(master = frame1)
    #解析网址
    label2 = Label(
        master = frame1,
        font = ("微软雅黑", 18),
        text = "解析网址："
    )
    label2.pack(
        anchor = "center",
        ipadx = width
    )
    def set_file_url() -> None:
        file_url = url
        label2.config(text = "解析网址：" + file_url)
        creater.set_file_url(file_url)
    btn1 = Button(
        master = frame13,
        command = set_file_url,
        font = ("微软雅黑", 12),
        text = "解析网址"
    )
    btn1.pack(
        side = "left",
        padx = 10
    )
    #保存路径
    label3 = Label(
        master = frame1,
        font = ("微软雅黑", 18),
        text = "保存路径："
    )
    label3.pack(
        anchor = "center",
        ipadx = width
    )
    def set_dir_name() -> None:
        dir_name = askdirectory(
            initialdir = "./",
            title = "保存路径"
        )
        creater.set_dir_name(dir_name)
        label3.config(text = "保存路径：" + dir_name)
    btn2 = Button(
        master = frame13,
        command = set_dir_name,
        font = ("微软雅黑", 12),
        text = "保存路径"
    )
    btn2.pack(
        side = "left",
        padx = 10
    )
    #生成地图
    def get_map_file() -> None:
        if hasattr(creater, "file_url") == False:
            return
        id_list = [check_btn1_var.get(), check_btn2_var.get(), check_btn3_var.get(), check_btn4_var.get()]
        if creater.get_map_file(id_list) == False:
            showerror("生成地图错误", "生成地图错误")
        else:
            if askyesno("是否打开生成地图的文件", "是否打开生成地图的文件") == True:
                path = "."
                if hasattr(creater, "dir_name") == True:
                    path = creater.dir_name
                for root, dir_list, file_list in os.walk(path):
                    for file in file_list:
                        if file.endswith(".html"):
                            webbrowser.open_new_tab(os.path.join(root, file))
                    break
    btn3 = Button(
        master = frame13,
        command = get_map_file,
        font = ("微软雅黑", 12),
        text = "生成地图"
    )
    btn3.pack(
        side = "left",
        padx = 10
    )
    frame13.pack(ipady = 20)
    root.mainloop()
def main() -> None:
    init("https://baike.baidu.com/item/第七次全国人口普查公报")
main()