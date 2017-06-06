# -*-  encoding:utf8 -*-
from lxml import etree
import requests
from multiprocessing.dummy import Pool
import re
import time
myheader = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
urls = []
html_str = ''
result_name_list= []
# result_describ_list = []
def get_sourse(url,header=myheader):
    html = requests.get(url,headers=header)
    time.sleep(1)
    return html.text

for i in range(1,10000):
    newpage = 'http://bangumi.bilibili.com/anime/'+ str(i)
    urls.append(newpage)
    if not requests.get(newpage):
        urls.remove(newpage)

pool = Pool(4)
result_html = pool.map(get_sourse,urls)
pool.close()
pool.join()

for i in result_html:
    html_str += str(i)
html = etree.HTML(html_str)
result_name = html.xpath('//title')
# result_describ = html.xpath('//meta/@content')
for i in result_name:
    result_name_list +=re.findall(r'(.*?)_番剧.*?',i.text)
# for i in result_describ_list:
#     result_describ_list += i


with open('spider.txt','w') as f:
    f.writelines([line+'\n' for line in result_name_list])
    # f.writelines([line+'\n' for line in result_describ_list])







