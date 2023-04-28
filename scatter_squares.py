# 使用scatter() 绘制一系列点
# 自动计算数据
import matplotlib.pyplot as plt

# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]
x_values = range(1, 1001)
y_values = [x ** 2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()

# ax.scatter(x_values, y_values, s = 10 , c = 'red')
# 要指定自定义颜色，可传递参数c ，并将其设置为一个元组，其中包含三个0～1的小数值，
# 分别表示红色、绿色和蓝色的分量。
# 值越接近0，指定的颜色越深；值越接近1，指定的颜色越浅。
# ax.scatter(x_values, y_values, c=(0, 0.8, 0), s=10)

# pyplot内置颜色映射
# 颜色映射 （colormap）是一系列颜色，从起始颜色渐变到结束颜色。在可视化中，颜色映射用于突出数据的规律。
# 将参数C设置成了一个y值列表，并使用参数cmap告诉pyplot 使用哪个颜色映射
ax.scatter(x_values ,  y_values , c = y_values , cmap = plt.cm.Reds , s = 10)

# 设置图表标题并给坐标轴加上标签
ax.set_title("平方数", fontsize=24)
ax.set_xlabel("值", fontsize=14)
ax.set_ylabel("值的平方", fontsize=14)

# 设置刻度标记的大小
ax.tick_params(axis = 'both' , which = 'major' , labelsize = 14)

# 设置每个坐标轴的取值范围
# 使用方法axis() 指定了每个坐标轴的取值范围。
# axis() 要求提供4个值：x和y坐标轴的最小值和最大值。
ax.axis([0 , 1100 , 0 , 1100000])

plt.rcParams['font.sans-serif']=['SimHei']  # 用来正常显示中文标签（中文乱码问题）

# plt.show()

# 要让程序自动将图表保存到文件中，可将调用plt.show() 替换为调用plt.savefig()
# 第一个实参指定要以什么文件名保存图表，这个文件将存储到scatter_squares.py所在的目录。
# 第二个实参指定将图表多余的空白区域裁剪掉
plt.savefig('squares_plot.png', bbox_inches='tight')