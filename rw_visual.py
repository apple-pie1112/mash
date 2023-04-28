import matplotlib.pyplot as plt

from random_walk import RandomWalk

# # 创建一个RandomWalk实例
# rw = RandomWalk()
# rw.fill_walk()
# # 将所有的点都绘制出来
# plt.style.use('classic')
# fig , ax = plt.subplots()
# # 将随机漫步包含的 值和 值传递给scatter()
# ax.scatter(rw.x_values , rw.y_values , s=15)
# plt.show()

# 只要程序处于活动状态，就不断地模拟随机漫步
while True:
    # 创建一个RandomWalk实例
    rw = RandomWalk(50000) # 包含50 000个点的随机漫步
    rw.fill_walk()

    # 将所有的点都绘制出来
    plt.style.use('classic')
        # 创建图表时，可传递参数figsize 以指定生成的图形的尺寸。单位为英寸
    fig , ax = plt.subplots(figsize=(15, 9))

    # 将随机漫步包含的x值和y值传递给scatter()
    # ax.scatter(rw.x_values , rw.y_values , s=15)
    point_number = range(rw.num_points)
    # 将参数c 设置为point_numbers ，指定使用颜色映射Blues ，
    # 并传递实参edgecolors='none' 以删除每个点周围的轮廓。
    # 最终的随机漫步图从浅蓝色渐变为深蓝色
    ax.scatter(rw.x_values, rw.y_values, c=point_number, cmap=plt.cm.Reds,
edgecolors='none', s=1)
    # pyplot内置颜色映射
    # 颜色映射 （colormap）是一系列颜色，从起始颜色渐变到结束颜色。在可视化中，颜色映射用于突出数据的规律。
    # 将参数C设置成了一个y值列表，并使用参数cmap告诉pyplot 使用哪个颜色映射

    # 突出起点和终点
    ax.scatter(0,0, c = 'green' , edgecolor='none' , s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='blue' ,edgecolors='none', s=100)

    # 隐藏坐标轴
    # 使用方法ax.get_xaxis()和ax.get_yaxis()将每条坐标轴的可见性都设置为False。
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    # 持续，重复，重新绘制随机漫步
    keep_running = input('Make another walk? (y/n):')
    if keep_running == 'n':
        break