# 使用scatter() 绘制散点图并设置样式
import matplotlib.pyplot as plt

plt.style.use('seaborn')
fig , ax = plt.subplots()
# 调用scatter() 并使用参数s 设置绘制图形时使用的点的尺寸
ax.scatter(2,4,s = 200) # 绘制单个点，向它传递一对x坐标和y坐标，它将在指定位置绘制一个点

# 设置图表标题并给坐标轴加上标签
ax.set_title("平方数", fontsize=24)
ax.set_xlabel("值", fontsize=14)
ax.set_ylabel("值的平方", fontsize=14)

# 设置刻度标记的大小
ax.tick_params(axis = 'both' , which = 'major' , labelsize = 14)

plt.rcParams['font.sans-serif']=['SimHei']  # 用来正常显示中文标签（中文乱码问题）

plt.show()