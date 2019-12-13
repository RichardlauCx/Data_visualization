# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : Richard_lau
#  @ file   : Richard.py
#  @ IDE    : PyCharm


import csv


filename = 'sitka_weather_12-2019.csv'
with open(filename, encoding='utf-8-sig') as f:  # 指定所读取编码格式
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

if __name__ == '__main__':
    pass