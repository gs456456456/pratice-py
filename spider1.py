# -*- coding:utf-8 -*-
import urllib.request
import urllib.parse
import pickle
response = urllib.request.urlopen("http://www.baidu.com")
print(response.read())
# values={}
# values['username'] = "1016903103@qq.com"
# values['password']="XXXX"

request = urllib.request.Request('http://www.xxxxx.com')
try:
    urllib.request.urlopen(request)
except urllib.request.URLError as e:
    print(e.reason())





