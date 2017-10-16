import os
import requests

print(os.getcwd())

r = requests.get("http://baidu.com")

print(r.url)
print(r.encoding)
print(r.text)
