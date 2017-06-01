import requests
import bs4
from bs4 import BeautifulSoup
import re


def get_page(n):
    if n > 95:
        return '你已经超出查找范围'
    else:
        urls = 'http://www.jikexueyuan.com/course/?pageNum=%s'%(n)
        head = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
        jike = requests.get(urls,headers = head)
        return jike.text

lesson_text = []
def spider(context):
    lesson_tag= re.findall(r'(<h2.*?fo-h2".*?</a></h2>)',context,re.X)
    for i in lesson_tag:
        soup = BeautifulSoup(i,'lxml')
        lesson_text.append(soup.a.string)
    return lesson_text


def main(n):
    a = []
    for x in range(1,n+1):
        if get_page:
            real = get_page(x)
            real2 = spider(real)
            for x in real2:
                a.append(x)
                b = list(zip(range(1000),a))
                print(b[len(b)-1])

if __name__ == '__main__':
    main(5)
