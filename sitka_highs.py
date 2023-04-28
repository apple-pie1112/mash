import csv
from datetime import datetime

import matplotlib.pyplot as plt


# filename = 'sitka_weather_07-2018_simple.csv'
filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    # 调用csv.reader() 并将前面存储的文件对象作为实参传递给它，从而创建一个与该文件相关联的阅读器对象。
    # 这个阅读器对象被赋给了reader 。
    reader = csv.reader(f)
    # 模块csv 包含函数next() ，调用它并传入阅读器对象时，它将返回文件中的下一行。
    header_row = next(reader)
    # print(header_row)
    # 获得每个元素的索引及其值
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    # 从文件中获取最高温度和日期
    highs = []
    dates = []
    # 由于已经读取了文件头行，这个循环将从第二行开始——从这行开始包含的是实际数据。
    for row in reader:
        current_date = datetime.strptime(row[2],'%Y-%m-%d')
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)
# print(highs)

    # 根据最高温度绘制图形
    plt.style.use('seaborn')
    fig , ax = plt.subplots()
    ax.plot(dates, highs , c='red')

    # 设置图形的格式
    # ax.set_title('2018年7月每日最高温度', fontsize=24)
    ax.set_title("2018年每日最高温度", fontsize=24)
    ax.set_xlabel('',fontsize=16)
    # 调用fig.autofmt_xdate() 来绘制倾斜的日期标签,以免其彼此重叠
    fig.autofmt_xdate()
    ax.set_ylabel("温度 (F)", fontsize=16)
    ax.tick_params(axis='both',which='major',labelsize=16)

    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签（中文乱码问题）
    plt.show()

