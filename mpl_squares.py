import matplotlib.pyplot as plt

input_values = [1,2,3,4,5]
# 创建了一个名为squares 的列表，在其中存储要用来制作图表的数据。
squares = [1, 4, 9, 16, 25]

# 使用matplotlib中已定义好的样式
plt.style.use('seaborn')
# 调用函数subplots()
# 这个函数可在一张图片中绘制一个或多个图表。
# 变量fig 表示整张图片。变量ax 表示图片中的各个图表，大多数情况下要使用它。
fig , ax = plt.subplots()
# 调用方法plot(),尝试根据给定的数据以有意义的方式绘制图表。
# 使用plot() 时可指定各种实参，还可使用众多函数对图形进行定制
ax.plot(input_values, squares , linewidth = 3)

# 设置图表标题并给坐标轴加上标签
# fontsize 指定图表中各种文字的大小
ax.set_title("平方数", fontsize = 24)
ax.set_xlabel("值", fontsize = 14)
ax.set_ylabel("值的平方", fontsize = 14)
# 设置刻度标记的大小
# 方法tick_params() 设置刻度的样式，其中
# 指定的实参将影响x轴和y轴上的刻度（axes='both' ），并将刻
# 度标记的字号设置为14（labelsize=14 ）
ax.tick_params(axis = 'both' , labelsize = 14)
# 在代码中添加如下语句 —— 设置字体为：SimHei（黑体）
plt.rcParams['font.sans-serif']=['SimHei']  # 用来正常显示中文标签（中文乱码问题）

plt.show()
