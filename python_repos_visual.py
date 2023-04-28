import requests

from plotly.graph_objs import Bar
from plotly import offline


url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

response_dict = r.json()
repo_dicts = response_dict['items']
# 新建一个空列表labels ，用于存储要给各个项目显示的文本
repo_links, stars, labels = [], [], []
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    # 从repo_dict 中取项目的URL，并将其赋给临时变量repo_url
    repo_url = repo_dict['html_url']
    # 创建一个指向项目的链接，为此使用了HTML标记<a>
    # 其格式为<a href='URL'>link text</a> 。
    # 然后，将这个链接附加到列表repo_links 末尾。
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    stars.append(repo_dict['stargazers_count'])

# 在处理数据的循环中，ᨀ 取每个项目的所有者和描述
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    # Plotly允许在文本元素中使用HTML代码，因此在创建
    # 由项目所有者和描述组成的字符串时，我们能够在这两部分之间添加换行符（<br /> ）
    label = f"{owner}<br />{description}"
    labels.append(label)

data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': 'Most-Starred Python Projects on GitHub',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },

}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')
