# 随机漫步：是这样行走得到的路径：每次行走都是完全随机的、没有明确的方向，结果是由一系列
# 随机决策决定的。
from random import choice

class RandomWalk:
    # 一个生成随机漫步的属性
    # 为模拟随机漫步，创建一个名为RandomWalk 的类，它随机地选择前进方向。
    # 这个类需要三个属性：一个是存储随机漫步次数的变量，其他两个是列表，
    # 分别存储随机漫步经过的每个点的x坐标和y坐标。
    def __init__(self , num_points = 5000):
        # 将随机漫步包含的默认点数设置为5000
        # 初始化随机漫步的属性
        self.num_points = num_points

        # 所有随机漫步都始于（0,0）
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        # 计算随机漫步包含的所有点

        # 不断漫步，直到列表达到指点的长度
        while len(self.x_values) < self.num_points:

            # 决定前进方向以及沿这个方向前进的距离
            x_direction = choice([1,-1]) # 右为1，左为-1
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # 拒绝原地踏步
            # 如果x_step 和y_step 都为零，则意味着原地踏步。接着执行下一次循环
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的x值和y值
            # 为获取漫步中下一个点的x值，将x_step 与x_values 中的最后一个值相加
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
