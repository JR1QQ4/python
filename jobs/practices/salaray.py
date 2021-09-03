#!/usr/bin/python
# -*- coding:utf-8 -*-
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyecharts
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple snapshot-selenium
import pyecharts
from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.render import make_snapshot

# 使用 snapshot-selenium 渲染图片
from snapshot_selenium import snapshot

# 劳动人口，单位万
people = {
    '2019': 81104,
    '2018': 80525,
    '2017': 80686,
    '2016': 80694,
    '2015': 80091,
    '2014': 79690,
    '2013': 79300,
    '2012': 78894,
    '2011': 78579,
    '2010': 78388,
    '2009': 77510,
    '2008': 77046,
    '2007': 76531,
    '2006': 76315,
    '2005': 76120,
    '2004': 75290,
    '2003': 74911,
    '2002': 74492,
    '2001': 73884
}

# print(pyecharts.__version__)

# 方法一
# bar = Bar()
# bar.add_xaxis([x + '年' for x in list(people.keys())[::-1]])
# bar.add_yaxis("劳动人口", [y for y in list(people.values())[::-1]])

# 方法二
# bar = (
#     Bar()
#     .add_xaxis([x + '年' for x in list(people.keys())[::-1]])
#     .add_yaxis("劳动人口数", [y for y in list(people.values())[::-1]])
#     .set_global_opts(title_opts=opts.TitleOpts(title="历年劳动人口变化", subtitle="单位（万人）"))
#     # 或者直接使用字典参数
#     # .set_global_opts(title_opts={"text": "主标题", "subtext": "副标题"})
# )

# 渲染成图片
# make_snapshot(snapshot, bar.render(), "bar.png")

# render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
# 也可以传入路径参数，如 bar.render("mycharts.html")
# bar.render()


class Population:
    def total_population(self):
        pass

    def population_rate(self):
        pass

    def population_structure(self):
        pass


class EmploymentStatusAndWages:
    def labor_force(self):
        pass

    def employment(self):
        pass

    def unemployment(self):
        pass

    def average_wage(self):
        pass











