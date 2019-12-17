# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : Richard_lau
#  @ file   : Richard.py
#  @ IDE    : PyCharm

from __future__ import (absolute_import, division, print_function, unicode_literals)


def urllib_module():
    try:
        from urllib2 import urlopen  # Python2.x 版本导入方法
    except ImportError:
        print("The current environment for Python3.x")
        from urllib.request import urlopen
    import json

    # 用Json格式实现数据下载
    json_url = 'http://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
    response = urlopen(json_url)
    req = response.read()  # 读取数据
    # urllib.error.URLError: <urlopen error [WinError 10060] 由于连接方在一段时间后没有正确答复或连接的主机没有反应，连接尝试失败。>
    with open('btc_close_2017_urllib.json', 'wb') as f:
        f.write(req)  # 将数据写入文件
    file_urllib = json.loads(req)  # 加载json格式，转化为Python能够处理的格式
    print(file_urllib)


def requests_module():
    import requests

    json_url = 'http://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
    req = requests.get(json_url)
    with open('btc_close_2017_urllib.json', 'w') as f:
        f.write(req.text)  # 将数据写入文件
    file_requests = req.json()
    print(file_requests)


def extract_json_data():
    import json
    file_name = 'btc_close_2017_urllib.json'  # TODO 看另一个文件情况
    with open(file_name) as f:
        btc_data = json.load(f)

    dates = []
    months = []
    weeks = []
    weekdays = []
    closes = []

    # 获取每一天的数据信息
    for btc_dic in btc_data:  # 从一个列表中拿多个字典
        dates.append(btc_dic['date'])
        months.append(int(btc_dic['month']))
        weeks.append(int(btc_dic['week']))
        weekdays.append(btc_dic['weekday'])
        closes.append(int(float((btc_dic['close']))))
        # print("{} is month {} week {}, {}, the close price is {} RMB".format(data, month, week, weekday, close))

    return dates, months, weeks, weekdays, closes


def using_py_gal(dates, closes):
    import pygal
    import math

    line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
    line_chart.title = '收盘价（￥）'
    line_chart.x_labels = dates
    n = 20  # x轴坐标每隔20天显示一次
    line_chart.x_labels_major = dates[::n]
    print(dates[::n])  # 可每隔20个数据获取一次
    # print(dates[:n])  # 获取前20个数据
    close_log = [math.log10(_) for _ in closes]
    line_chart.add('收盘价', close_log)
    line_chart.render_to_file('收盘价折线图（￥）.svg')


def semi_logarithmic(dates, closes):
    import math
    import pygal

    line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
    line_chart.title = '收盘价对数变化（￥）'
    line_chart.x_labels = dates
    n = 20  # 同样的x轴坐标值每隔20天显示一次
    line_chart.x_labels_major = dates[::n]
    close_log = [math.log10(_) for _ in closes]  # 数据拿到下划线当中，并且进入前面的计算，计算完之后作为列表元素
    line_chart.add('log收盘价', close_log)
    line_chart.render_to_file('收盘价对数变换折线图（￥）.svg')


def draw_line(x_data, y_data, title, y_legend):
    import pygal
    from itertools import groupby

    xy_map = []  # x,y的相关映射数据
    for x, y in groupby(sorted(zip(x_data, y_data)), key=lambda _: _[0]):  # 对应取第一个元素进行压缩排序，后分组  # TODO 考究
        y_list = [v for _, v in y]
        xy_map.append([x, sum(y_list) / len(y_list)])  # 总和除以长度为平均值
    x_unique, y_mean = [*zip(*xy_map)]  # TODO 解决不规范变黄问题
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_legend, y_mean)
    line_chart.render_to_file(title + '.svg')
    return line_chart  # 返回折线统计图对象


def dash_board():
    with open('收盘价Dashboard.html', 'w', encoding='utf-8') as html_file:
        html_file.write('<html><head><title>收盘价Dashboard</title><meta charset="utf-8"></head><body>\n')
        for svg in [
            '收盘价折线图（￥）.svg', '收盘价对数变换折线图.svg', '收盘价月日均值（￥）.svg',
            '收盘价周日均值（￥）.svg', '收盘价星期均值（￥）.svg'
        ]:
            html_file.write('    <object type="image/svg+xml" data="{0}" height=500></object>\n'.format(svg))
        html_file.write('</body></html>')


if __name__ == '__main__':
    # urllib_module()··
    # requests_module()
    date, month, week, weekday, close = extract_json_data()
    # using_py_gal(date, close)
    # semi_logarithmic(date, close)

    # idx_month = date.index('2017-12-01')
    # line_chart_month = draw_line(month[:idx_month], close[:idx_month], '收盘价月日均值（￥）', '月日均值')

    # idx_week = date.index('2017-12-11')
    # line_chart_week = draw_line(week[1:idx_week], close[1:idx_week], '收盘价周日均值（￥）', '周日均值')

    # idx_week = date.index('2017-12-11')
    # wd = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']  # 相当于字典功能
    # weekdays_int = [wd.index(w) + 1 for w in weekday[1: idx_week]]
    # line_chart_weekday = draw_line(weekdays_int, close[1:idx_week], '收盘价星期均值（￥）', '星期均值')
    # # x轴默认会根据数据，从小到大排序
    # line_chart_weekday.x_labels = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
    # line_chart_weekday.render_to_file('收盘价星期均值（￥）.svg')

    # dash_board()
