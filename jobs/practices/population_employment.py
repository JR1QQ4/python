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

import os
import yaml

date_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'datas')
population_yaml = os.path.join(date_path, 'population.yaml')
employment_yaml = os.path.join(date_path, 'employment.yaml')
# print(population_yaml)
# print(employment_yaml)

population_data = yaml.safe_load(open(population_yaml))
employment_data = yaml.safe_load(open(employment_yaml))

# print(population_data['Population'])
# print(employment_data['EmploymentStatusAndWages'])

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


def my_render(items: dict, y_name='y轴名称', title='标题', subtitle='副标题', filepath='mycharts.html', payload_str=''):
    bar = (
        Bar()
        .add_xaxis([x + payload_str for x in list(items.keys())[::-1]])
        .add_yaxis(y_name, [y for y in list(items.values())[::-1]], bar_width='50%')
        .set_global_opts(title_opts=opts.TitleOpts(title=title, subtitle=subtitle))
    )
    bar.render(filepath)


total_population = population_data['Population']['total_population']
my_render(total_population, y_name='年末总人口(万人)', title='总人口', subtitle='副标题',
          filepath='outputs/total_population.html', payload_str='年')


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
