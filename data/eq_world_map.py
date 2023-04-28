# Plotly Express是Plotly的高级接口，简单易用，语法与Matplotlib类似
import plotly.express as px

fig = px.scatter(
    x = lons,
    y = lats,
    labels = {'x':'经度' , 'y':'纬度'},
    range_x = [-200 , 200],
    range_y = [-90 , 90],
    width = 800,
    height = 800,
    title = '全球地震散点图',
)
fig.write_html('global_earthquakes.html')
fig.show()
