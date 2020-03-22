import  requests
import  json
from  selenium.common.exceptions import  *
import  logging
import  os
import  logging.config
path=os.path.dirname(os.getcwd())
print(path)
path=os.path.join(path,'test_log','log.conf')

logging.config.fileConfig(path)
logging = logging.getLogger()

#请求类
class requ(object):
    def __init__(self):
        self.header={'Content-Type': 'application/json'}

    #get 请求
    def getRe(self,url,params):
        try:
            r=requests.get(url,params=params,headers=self.header)
            r.encoding='UTF-8'
            json_response=json.loads(r.text)
            #print(type(json_response))
            return {'code':'0','result':json_response}
        except Exception as  e:
            logging.info("get 请求出错，出错原因: %s"%e)

            return {'code':'0','result':"get 请求出错，出错原因: %s"%e}

    #post请求
    def postRe(self,url,params):
        try:

            re=requests.post(url,data=json.dumps(params),headers=self.header,verify=False)
            print(re.text)
            json_response=json.loads(re.text)
            print('re %s' % json_response)
            return {'code': 0, 'result': json_response}
        except Exception as e:
            logging.info('post请求出错，出错原因:%s' % e)
            return {'code': 1, 'result': 'post请求出错，出错原因:%s' % e}


if __name__ == '__main__':
    re=requ()
    url='http://wthrcdn.etouch.cn:80/weather_mini'
    dict={
            "city":"北京"
         }

    print(type(dict))
    # r=re.getRe(url,dict)
    # print(r)
    res=re.postRe(url,dict)
    print(res)


