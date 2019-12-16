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

    return dates, closes


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

    # TODO x坐标轴上面数据异常


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


if __name__ == '__main__':
    # urllib_module()
    # requests_module()
    date, close = extract_json_data()
    using_py_gal(date, close)
    semi_logarithmic(date, close)
