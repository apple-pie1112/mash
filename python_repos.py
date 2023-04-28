# WEB API
import requests

# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
# 调用get() 并将URL传递给它，再将响应对象赋给变量r 。
r = requests.get(url, headers=headers)
# 响应对象包含一个名为status_code 的属性，指出了请求是否成功（状态码200表示请求成功）
print(f'Status code:{r.status_code}')
# 将API响应赋给一个变量
# 使用方法json() 将这些信息转换为一个Python字典
response_dict = r.json()
print(f"Total repositories:{response_dict['total_count']}")

# 探索有关仓库的信息
repo_dicts = response_dict['items']
print(f"Repositories returned:{len(repo_dicts)}")


# 研究第一个仓库
# repo_dict = repo_dicts[0]
# print(f"\nKeys: {len(repo_dict)}")
# for key in sorted(repo_dict.keys()):
#     print(key)

# 打印一条说明性信息
print("\nSelected information about first repository:")
for repo_dict in repo_dicts:
    # 打印了项目的名称
    print(f"Name:{repo_dict['name']}")
    # 项目所有者是由一个字典表示的,再使用键key 来获取所有者的登录名
    print(f"Owner: {repo_dict['owner']['login']}")
    # 打印项目获得了多少个星的评级
    print(f"Stars: {repo_dict['stargazers_count']}")
    # GitHub仓库的URL
    print(f"Repository: {repo_dict['html_url']}")
    # 显示项目的创建时间
    print(f"Created: {repo_dict['created_at']}")
    # 最后一次更新的时间
    print(f"Updated: {repo_dict['updated_at']}")
    # 打印仓库的描述
    print(f"Description: {repo_dict['description']}")
# 处理结果
# print(response_dict.keys())