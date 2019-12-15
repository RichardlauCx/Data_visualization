# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : Richard_lau
#  @ file   : Richard.py
#  @ IDE    : PyCharm


import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'sitka_weather_12-2019.csv'  # 因为是同级下的，所以不需要强调路径
title = "Daily high and low temperatures - 2019, CA"
with open(filename, encoding='utf-8-sig') as f:  # 指定所读取编码格式
    reader = csv.reader(f)  # 读取到的数据为'_csv.reader'对象，不能直接访问
    # header_row = next(reader)  # 每次next读取下一行
    # print(header_row)

    # for index, column_header in enumerate(header_row):  # column为列
    #    print(index, column_header)
    #    pass

    # print(reader)

# 从文件中获取日期、最高气温和最低气温

    dates, highs, lows = [], [], []
    for row in reader:  # 拿出阅读器所存储的余下各行（一行为一个列表）
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])  # 使其变为整型数据列表
            low = int(row[3])
        except ValueError:
            print(current_date, 'Missing data')
        else:
            dates.append(current_date)
            highs.append(high)  # 以索引出来的数据，作为参数添加进列表
            lows.append(low)
        # print(row[1])
        # pass

    # 根据数据绘制图像
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highs, c='red', alpha=0.5)  # 第一个参数为x轴，第二个参数为y轴
    plt.plot(dates, lows, c='blue', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
    plt.title(title, fontsize=20)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature(F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

    # TODO: 如何将坐标轴上面数据量加大
