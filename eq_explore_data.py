import json
import plotly.express as px
import pandas as pd
# 探索数据的结构
# filename = 'data/eq_data_1_day_m1.json'
filename = 'data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

readable_file = 'data/readable_eq_data.json'
with open(readable_file,'w') as f:
    # json.dump() 接受一个JSON数据对象和一个文件对象，并将数据写入这个文件中
    # 参数indent=4 让dump()使用与数据结构匹配的缩进量来设置数据的格式。
    json.dump(all_eq_data , f , indent=4)

all_eq_dicts = all_eq_data['features']
# print(len(all_eq_dicts))

# 提取震级,位置数据
mags , titles , lons , lats = [] , [] , [] , []
for eq_dict in all_eq_dicts:
    # 每次地震的震级都存储在相应字典的'properties' 部分的'mag' 键下
    mag = eq_dict['properties']['mag']
    title = eq_dict['properties']['title']
    # 代码eq_dict['geometry'] 访问与"geometry" 键相关联的字典
    # 第二个键('coordinates')取与"coordinates" 相关联的列表，而索
    # 引0,取该列表中的第一个值，即地震发生位置的经度。
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)

# print([mags[:10]])
# print(titles[:2])
# print(lons[:5])
# print(lats[:5])

data = pd.DataFrame(
data=zip(lons, lats, titles, mags), columns=["经度", "纬度", "位置", "震级"]
)
data.head()

fig = px.scatter(
    data,
    x = '经度',
    y = '纬度',
    # x = lons,
    # y = lats,
    # labels = {'x':'经度' , 'y':'纬度'},
    range_x = [-200 , 200],
    range_y = [-90 , 90],
    width = 800,
    height = 800,
    title = '全球地震散点图',
    # 使用了size 参数来指定散点图中每个标记的尺寸
    size = '震级',
    size_max = 10,
    # 默认的视觉映射图例渐变色范围是从蓝到红再到黄，数值越小则标记越蓝，而数值越大则标记越黄
    color="震级",
    # 添加说明性文本
    # 将鼠标指向表示地震的标记时显示出来。除了默认显示的经度和纬度外，还将显示震级以及地震的大致位置
    hover_name="位置",
)
fig.write_html('global_earthquakes.html')
fig.show()
