from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# 创建一个D6 (骰子是根据面数命名的，6面的骰子名为D6，8面的骰子名为D8，依此类推。)
die = Die()

# 掷几次骰子并将结果存储在一个列表中
results = []
# 掷骰子100次，并将每次的结果都存储在列表results 中。
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# 分析结果
frequencies = []
for value in range(1 , die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)
# print(frequencies)

# 对结果进行可视化
# 绘制直方图
# Plotly不能直接接受函数range() 的结果，因此需要使用函数list() 将其转换为列表。
x_values = list(range(1 , die.num_sides + 1))
# Plotly类Bar() 表示用于绘制条形图的数据集,需要一个存储x值的列表和一个存储y值的列表。
# 这个类必须放在方括号内，因为数据集可能包含多个元素
data = [Bar(x=x_values , y=frequencies)]

x_axis_config = {'title':'结果'}
y_axis_config = {'title':'结果的频率'}
# 类Layout()返回一个指定图表布局和配置的对象。这里设置了图表名称，并传入了x轴和y轴的配置字典。
my_layout = Layout(title = '掷一个D6 1000次的结果' , xaxis = x_axis_config , yaxis = y_axis_config)
# 为生成图表，调用了函数offline.plot().
# 这个函数需要一个包含数据和布局对象的字典，还接受一个文件名，指定要将图表保存到哪里。这里将输出存储到文件d6.html。
offline.plot({'data':data , 'layout':my_layout} , filename='d6.html')