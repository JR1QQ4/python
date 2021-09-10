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
                             axistick_opts=opts.AxisTickOpts(
                                 length=10,
                             ),

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
                             name_textstyle_opts=opts.TextStyleOpts(
                                 font_size=12,
                             ),

                             # 分割区域配置项，参考 `series_options.SplitAreaOpts`
                             # splitarea_opts: Union[SplitAreaOpts, dict, None] = None,

                             # 分割线配置项，参考 `series_options.SplitLineOpts`
                             # splitline_opts: Union[SplitLineOpts, dict] = SplitLineOpts(),

                             # 坐标轴次刻度线相关设置，参考 `series_options.MinorTickOpts`
                             # minor_tick_opts: Union[MinorTickOpts, dict, None] = None,

                             # 坐标轴在 grid 区域中的次分隔线。次分割线会对齐次刻度线 minorTick，参考 `series_options.MinorSplitLineOpts`
                             # minor_split_line_opts: Union[MinorSplitLineOpts, dict, None] = None
                         ),
                         visualmap_opts=opts.VisualMapOpts(
                             # 是否显示视觉映射配置
                             # is_show: bool = True,
                             is_show=True,

                             # 映射过渡类型，可选，"color", "size"
                             # type_: str = "color",

                             # 指定 visualMapPiecewise 组件的最小值。
                             # min_: Union[int, float] = 0,

                             # 指定 visualMapPiecewise 组件的最大值。
                             # max_: Union[int, float] = 100,

                             # 两端的文本，如['High', 'Low']。
                             # range_text: Union[list, tuple] = None,

                             # visualMap 组件过渡颜色
                             # range_color: Union[Sequence[str]] = None,

                             # visualMap 组件过渡 symbol 大小
                             # range_size: Union[Sequence[int]] = None,

                             # visualMap 图元以及其附属物（如文字标签）的透明度。
                             # range_opacity: Optional[Numeric] = None,

                             # 如何放置 visualMap 组件，水平（'horizontal'）或者竖直（'vertical'）。
                             # orient: str = "vertical",

                             # visualMap 组件离容器左侧的距离。
                             # left 的值可以是像 20 这样的具体像素值，可以是像 '20%' 这样相对于容器高宽的百分比，
                             # 也可以是 'left', 'center', 'right'。
                             # 如果 left 的值为'left', 'center', 'right'，组件会根据相应的位置自动对齐。
                             # pos_left: Optional[str] = None,

                             # visualMap 组件离容器右侧的距离。
                             # right 的值可以是像 20 这样的具体像素值，可以是像 '20%' 这样相对于容器高宽的百分比。
                             # pos_right: Optional[str] = None,

                             # visualMap 组件离容器上侧的距离。
                             # top 的值可以是像 20 这样的具体像素值，可以是像 '20%' 这样相对于容器高宽的百分比，
                             # 也可以是 'top', 'middle', 'bottom'。
                             # 如果 top 的值为'top', 'middle', 'bottom'，组件会根据相应的位置自动对齐。
                             # pos_top: Optional[str] = None,

                             # visualMap 组件离容器下侧的距离。
                             # bottom 的值可以是像 20 这样的具体像素值，可以是像 '20%' 这样相对于容器高宽的百分比。
                             # pos_bottom: Optional[str] = None,

                             # 对于连续型数据，自动平均切分成几段。默认为5段。连续数据的范围需要 max 和 min 来指定
                             # split_number: int = 5,

                             # 指定取哪个系列的数据，默认取所有系列。
                             # series_index: Union[Numeric, Sequence, None] = None,

                             # 组件映射维度
                             # dimension: Optional[Numeric] = None,

                             # 是否显示拖拽用的手柄（手柄能拖拽调整选中范围）。
                             # is_calculable: bool = True,

                             # 是否为分段型
                             # is_piecewise: bool = False,

                             # 是否反转 visualMap 组件
                             # is_inverse: bool = False,

                             # 数据展示的小数精度。
                             # 连续型数据平均分段，精度根据数据自动适应。
                             # 连续型数据自定义分段或离散数据根据类别分段模式，精度默认为0（没有小数）。
                             # precision: Optional[int] = None,

                             # 自定义的每一段的范围，以及每一段的文字，以及每一段的特别的样式。例如：
                             # pieces: [
                             #   {"min": 1500}, // 不指定 max，表示 max 为无限大（Infinity）。
                             #   {"min": 900, "max": 1500},
                             #   {"min": 310, "max": 1000},
                             #   {"min": 200, "max": 300},
                             #   {"min": 10, "max": 200, "label": '10 到 200（自定义label）'},
                             #   {"value": 123, "label": '123（自定义特殊颜色）', "color": 'grey'}, //表示 value 等于 123 的情况
                             #   {"max": 5}     // 不指定 min，表示 min 为无限大（-Infinity）。
                             # ]
                             # pieces: Optional[Sequence] = None,

                             # 定义 在选中范围外 的视觉元素。（用户可以和 visualMap 组件交互，用鼠标或触摸选择范围）
                             #  可选的视觉元素有：
                             #  symbol: 图元的图形类别。
                             #  symbolSize: 图元的大小。
                             #  color: 图元的颜色。
                             #  colorAlpha: 图元的颜色的透明度。
                             #  opacity: 图元以及其附属物（如文字标签）的透明度。
                             #  colorLightness: 颜色的明暗度，参见 HSL。
                             #  colorSaturation: 颜色的饱和度，参见 HSL。
                             #  colorHue: 颜色的色调，参见 HSL。
                             # out_of_range: Optional[Sequence] = None,

                             # 图形的宽度，即长条的宽度。
                             # item_width: int = 0,

                             # 图形的高度，即长条的高度。
                             # item_height: int = 0,

                             # visualMap 组件的背景色。
                             # background_color: Optional[str] = None,

                             # visualMap 组件的边框颜色。
                             # border_color: Optional[str] = None,

                             # visualMap 边框线宽，单位px。
                             # border_width: int = 0,

                             # 文字样式配置项，参考 `series_options.TextStyleOpts`
                             # textstyle_opts: Union[TextStyleOpts, dict, None] = None,
                         ),
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
