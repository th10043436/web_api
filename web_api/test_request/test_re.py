# !/usr/bin/env python
# -*- coding: utf-8 -*-
import  requests
import  json
from  selenium.common.exceptions import  *
import  logging
import  os
import  logging.config
import  demjson
path=('111111111111'+os.getcwd())
print(path)
path11=os.path.dirname(os.path.dirname(__file__))
print('ffffffffffff' + path11)

path_01=os.path.join(path,'test_log','log.conf')
logging.config.fileConfig(path11+'/test_log/log.conf')
logging = logging.getLogger()

#请求类
class requ(object):
    def __init__(self):
        self.get_header={'Content-Type': 'application/json'}

    #get 请求
    def getRe(self,url,params=None):
        try:
            r=requests.get(url,params=params)
            r.encoding='UTF-8'
            json_response=json.loads(r.text)
            #print(type(json_response))
            return {'code':'0','result':json_response}
        except Exception as  e:
            logging.info("get 请求出错，出错原因: %s"%e)

            return {'code':'0','result':"get 请求出错，出错原因: %s"%e}

    #post请求
    def postRe(self,url,params=None):# 这里有个细节，如果body需要json形式的话，需要做处理, 可以用data = json.dumps(body)
        data1 = json.dumps(params)
        try:

            re=requests.post(url,json=params,headers=self.get_header,verify=False)
            print(re.text)
            json_response=json.loads(re.text)
            print('re %s' % json_response)
            return {'code': 0, 'result': json_response}
        except Exception as e:
            logging.info('post请求出错，出错原因:%s' % e)
            return {'code': 1, 'result': 'post请求出错，出错原因:%s' % e}
    #put请求
    def putRe(self,url,params):
        data1=json.dumps(params)
        try:
            re=requests.put(url,data=data1,headers=self.get_header)
            re_put=json.loads(re.text)

            return  {'code':'0','result':re_put}

        except Exception as error:
            logging.info('put 请求出错,出错原因: {}'.format(error))
            return {'code': 1, 'result': 'post请求出错，出错原因:%s' % error}

    def deleteRe(self,url,params):#删除的请求
        try:
            del_word=requests.delete(url,params=params,headers=self.get_header)
            json_response=json.loads(del_word.text)
            return {'code': 0, 'result': json_response}
        except Exception as e:
            logging.info('del请求出错，出错原因:%s' % e)
            return {'code': 1, 'result': 'del请求出错，出错原因:%s' % e}

if __name__ == '__main__':
    path = os.path.dirname(os.getcwd())
    print('----------------' + path)
    re=requ()
    url='http://wthrcdn.etouch.cn:80/weather_mini'
    dict_post={'city':"北京"}
    r=re.getRe(url,dict_post)
    print(r)
    # print(type(r))
    #res=re.postRe(url,dict_post)
    #print(res)
    #re.putRe(url,dict_post)





