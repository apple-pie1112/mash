import csv
from datetime import datetime

import matplotlib.pyplot as plt
filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # for index, column_header in enumerate(header_row):
    #     print(index , column_header)

    # 从文件中获取日期，最高温度和最低温度
    dates , highs , lows = [] , [] , []
    for row in reader:
        current_date = datetime.strptime(row[2] , '%Y-%m-%d')
        try: # 对可能出现的异常进行处理
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f'Missing data for {current_date}')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    # 根据最高温度和最低温度绘制图形
    plt.style.use('seaborn')
    fig , ax = plt.subplots()
    # alpha 指定颜色的透明度.alpha 值为0表示完全透明，为1（默认设置）表示完全不透明
    ax.plot(dates , highs , c='red' , alpha=0.5)
    ax.plot(dates , lows , c='blue' , alpha=0.5)
    # 实参facecolor指定填充区域的颜色
    ax.fill_between(dates , highs , lows , facecolor='blue' , alpha=0.1)

    # 设置图形的格式
    # ax.set_title("2018年每日最高温度", fontsize=24)
    title = '2018年每日最高温度和最低温度\n美国加利福尼亚州死亡谷'
    ax.set_title(title , fontsize = 20)
    ax.set_xlabel('', fontsize=16)
    # 调用fig.autofmt_xdate() 来绘制倾斜的日期标签,以免其彼此重叠
    fig.autofmt_xdate()
    ax.set_ylabel("温度 (F)", fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)

    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签（中文乱码问题）
    plt.show()
