#-*- encoding:utf-8 -*-
import requests
from wxpy import *
import wxpy
import json
def talk_robet(info = '少年或少女的外号'):
    api_url= 'http://www.tuling123.com/openapi/api'
    apikey = '4d31adf92c704733aa5b833ef9955f96'
    data = {'key': apikey,'info': info}
    req = requests.post(api_url, data=data).text
    replys = json.loads(req)['text']
    return replys

robot = Bot()
my_friend = robot.friends().search('XXX',sex = MALE)[0]
@robot.register(my_friend)
def reply_my_friend(msg):
    message = '{}'.format(msg.text)
    replys = talk_robet(info=message)
    return replys

robot.join()

