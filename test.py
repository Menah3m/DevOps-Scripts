# import psutil

# a = psutil.virtual_memory()

# print(a.percent/100)

import requests

r = requests.get("http://www.baidu.com")
print(r.headers)