# -*- coding:utf-8 -*-
import urllib.request
import urllib.parse
import re
import time
class QBspider():

    def __init__(self,index):
        self.index = index
        self.page_content = []


    def get_imform(self,index):
        url = 'http://www.qiushibaike.com/hot/page/' +str(self.index)
        header = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
        try:
             request = urllib.request.Request(url,headers = header)
             response = urllib.request.urlopen(request)
             content = response.read().decode('utf-8')
             return content
        except urllib.request.URLError as e:
               if hasattr(e,'code'):
                    print('打开网页有误,错误代码%s'%(e.code))
                    return None

    def print_content(self,index,page_content):
        pagecode = self.get_imform(index)
        P1 = re.compile('<h2>(.*?)</h2>.*?content">(.*?)</span>.*?number">(.*?)</i>',re.S)
        items = re.findall(P1,pagecode)
        for item in items:
            self.page_content.append('用户名:'+item[0].strip()+'    内容:'+item[1].strip()+'    点赞数:'+item[2].strip(),)
        return (self.page_content)

    def main(self):
        a = []
        if self.get_imform:
            for x in range(1,self.index+1):
                time.sleep(3)
                imfo = self.get_imform(x)
                imfo2 = self.print_content(x,imfo)
                for x in imfo2:
                    a.append(x)

        with open('record.txt','w') as f:
            f.writelines([line+'\n' for line in a])
        return


if __name__ =='__main__':
      a = QBspider(3)
      a.main()