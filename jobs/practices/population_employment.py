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
        .set_global_opts(title_opts=opts.TitleOpts(title=title, subtitle=subtitle),
                         yaxis_opts=opts.AxisOpts(name="我是Y轴"),
                         xaxis_opts=opts.AxisOpts(
                             # 坐标轴类型。可选：
                             # 'value': 数值轴，适用于连续数据。
                             # 'category': 类目轴，适用于离散的类目数据，为该类型时必须通过 data 设置类目数据。
                             # 'time': 时间轴，适用于连续的时序数据，与数值轴相比时间轴带有时间的格式化，在刻度计算上也有所不同，
                             # 例如会根据跨度的范围来决定使用月，星期，日还是小时范围的刻度。
                             # 'log' 对数轴。适用于对数数据。
                             # type_: Optional[str] = None,
                             type_='category',

                             # 坐标轴名称。
                             # name: Optional[str] = None,
                             name='这是X轴',

                             # 是否显示 x 轴。
                             # is_show: bool = True,

                             # 只在数值轴中（type: 'value'）有效。
                             # 是否是脱离 0 值比例。设置成 true 后坐标刻度不会强制包含零刻度。在双数值轴的散点图中比较有用。
                             # 在设置 min 和 max 之后该配置项无效。
                             # is_scale: bool = False,

                             # 是否反向坐标轴。
                             # is_inverse: bool = False,

                             # 坐标轴名称显示位置。可选：
                             # 'start', 'middle' 或者 'center','end'
                             # name_location: str = "end",
                             name_location='end',

                             # 坐标轴名称与轴线之间的距离。
                             # name_gap: Numeric = 15,

                             # 坐标轴名字旋转，角度值。
                             # name_rotate: Optional[Numeric] = None,

                             # 强制设置坐标轴分割间隔。
                             # 因为 splitNumber 是预估的值，实际根据策略计算出来的刻度可能无法达到想要的效果，
                             # 这时候可以使用 interval 配合 min、max 强制设定刻度划分，一般不建议使用。
                             # 无法在类目轴中使用。在时间轴（type: 'time'）中需要传时间戳，在对数轴（type: 'log'）中需要传指数值。
                             # interval: Optional[Numeric] = None,

                             # x 轴所在的 grid 的索引，默认位于第一个 grid。
                             # grid_index: Numeric = 0,

                             # x 轴的位置。可选：
                             # 'top', 'bottom'
                             # 默认 grid 中的第一个 x 轴在 grid 的下方（'bottom'），第二个 x 轴视第一个 x 轴的位置放在另一侧。
                             # position: Optional[str] = None,

                             # Y 轴相对于默认位置的偏移，在相同的 position 上有多个 Y 轴的时候有用。
                             # offset: Numeric = 0,

                             # 坐标轴的分割段数，需要注意的是这个分割段数只是个预估值，最后实际显示的段数会在这个基础上根据分割后坐标轴刻度显示的易读程度作调整。
                             # 默认值是 5
                             # split_number: Numeric = 5,

                             # 坐标轴两边留白策略，类目轴和非类目轴的设置和表现不一样。
                             # 类目轴中 boundaryGap 可以配置为 true 和 false。默认为 true，这时候刻度只是作为分隔线，
                             # 标签和数据点都会在两个刻度之间的带(band)中间。
                             # 非类目轴，包括时间，数值，对数轴，boundaryGap是一个两个值的数组，分别表示数据最小值和最大值的延伸范围
                             # 可以直接设置数值或者相对的百分比，在设置 min 和 max 后无效。 示例：boundaryGap: ['20%', '20%']
                             # boundary_gap: Union[str, bool, None] = None,

                             # 坐标轴刻度最小值。
                             # 可以设置成特殊值 'dataMin'，此时取数据在该轴上的最小值作为最小刻度。
                             # 不设置时会自动计算最小值保证坐标轴刻度的均匀分布。
                             # 在类目轴中，也可以设置为类目的序数（如类目轴 data: ['类A', '类B', '类C'] 中，序数 2 表示 '类C'。
                             # 也可以设置为负数，如 -3）。
                             # min_: Union[Numeric, str, None] = None,

                             # 坐标轴刻度最大值。
                             # 可以设置成特殊值 'dataMax'，此时取数据在该轴上的最大值作为最大刻度。
                             # 不设置时会自动计算最大值保证坐标轴刻度的均匀分布。
                             # 在类目轴中，也可以设置为类目的序数（如类目轴 data: ['类A', '类B', '类C'] 中，序数 2 表示 '类C'。
                             # 也可以设置为负数，如 -3）。
                             # max_: Union[Numeric, str, None] = None,

                             # 自动计算的坐标轴最小间隔大小。
                             # 例如可以设置成1保证坐标轴分割刻度显示成整数。
                             # 默认值是 0
                             # min_interval: Numeric = 0,

                             # 自动计算的坐标轴最大间隔大小。
                             # 例如，在时间轴（（type: 'time'））可以设置成 3600 * 24 * 1000 保证坐标轴分割刻度最大为一天。
                             # max_interval: Optional[Numeric] = None,

                             # 坐标轴刻度线配置项，参考 `global_options.AxisLineOpts`
                             # axisline_opts: Union[AxisLineOpts, dict, None] = None,

                             # 坐标轴刻度配置项，参考 `global_options.AxisTickOpts`
                             # axistick_opts: Union[AxisTickOpts, dict, None] = None,

                             # 坐标轴标签配置项，参考 `series_options.LabelOpts`
                             # axislabel_opts: Union[LabelOpts, dict, None] = None,
                             axislabel_opts=opts.LabelOpts(
                                 rotate=-45,
                                 interval=0,
                                 
                             ),

                             # 坐标轴指示器配置项，参考 `global_options.AxisPointerOpts`
                             # axispointer_opts: Union[AxisPointerOpts, dict, None] = None,

                             # 坐标轴名称的文字样式，参考 `series_options.TextStyleOpts`
                             # name_textstyle_opts: Union[TextStyleOpts, dict, None] = None,

                             # 分割区域配置项，参考 `series_options.SplitAreaOpts`
                             # splitarea_opts: Union[SplitAreaOpts, dict, None] = None,

                             # 分割线配置项，参考 `series_options.SplitLineOpts`
                             # splitline_opts: Union[SplitLineOpts, dict] = SplitLineOpts(),

                             # 坐标轴次刻度线相关设置，参考 `series_options.MinorTickOpts`
                             # minor_tick_opts: Union[MinorTickOpts, dict, None] = None,

                             # 坐标轴在 grid 区域中的次分隔线。次分割线会对齐次刻度线 minorTick，参考 `series_options.MinorSplitLineOpts`
                             # minor_split_line_opts: Union[MinorSplitLineOpts, dict, None] = None
                         )
        )
    )
    print(bar.options)
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
