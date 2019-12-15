# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : Richard_lau
#  @ file   : Richard.py
#  @ IDE    : PyCharm


import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'sitka_weather_12-2019.csv'
with open(filename, encoding='utf-8-sig') as f:  # 指定所读取编码格式
    reader = csv.reader(f)  # 读取到的数据为'_csv.reader'对象，不能直接访问
    # header_row = next(reader)  # 每次next读取下一行
    # print(header_row)

    # for index, column_header in enumerate(header_row):  # column为列
    #    print(index, column_header)
    #    pass

    # print(reader)

# 从文件中获取日期和最高气温

    dates, highs = [], []
    for row in reader:  # 拿出阅读器所存储的余下各行（一行为一个列表）
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        high = int(row[1])  # 使其变为整型数据列表
        highs.append(high)  # 以索引出来的数据，作为参数添加进列表
        # print(row[1])
        # pass

    # 根据数据绘制图像
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highs, c='red')  # 第一个参数为x轴，第二个参数为y轴
    plt.title("Daily high temperatures, July 2019", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature(F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

    # TODO: 如何将坐标轴上面数据量加大
