from  test_excel.read_excel import readEx
import  logging
import  os
import  logging.config
from  test_request.test_re import requ
path11=os.path.dirname(os.path.dirname(__file__))
logging.config.fileConfig(path11+'/test_log/log.conf')
logging = logging.getLogger()

class readData(object):
    def __init__(self,path):
        self.path=path
    def excelApi(self):
        read = readEx(self.path)  # 实例化读取表格类
        re = read.read_ex()
        logging.info('excel读取数据正确' + '------' + '{}'.format(re))
        ru = requ()  #
        list=[]
        for i in range(len(re)):
            r = re[i]['请求类型']
            if r == 'post':
                logging.info(re[i]['url'] + '==get==' + re[i]['参数'])
                params = re[i]['参数']
                if params != '':
                    print(type(eval(params)))
                    params = eval(params)  # 把params字符串转化为字典
                    get = ru.getRe(re[i]['url'], params)
                    # print('-----------'+str(get))
                    list.append(get)
                else:
                    po = ru.getRe(re[i]['url'], params)
                    # print('------------'+str(po))
                    list.append(po)

            else:
                logging.info(re[i]['url'] + '==get==' + re[i]['参数'])
                params = re[i]['参数']
                if params != '':
                    print(type(eval(params)))
                    params = eval(params)  # 把params字符串转化为字典
                    get = ru.getRe(re[i]['url'], params)
                    #print('-----------'+str(get))
                    list.append(get)
                else:
                    po= ru.getRe(re[i]['url'], params)
                    #print('------------'+str(po))
                    list.append(po)
        return list



if __name__ == '__main__':
    data=readData(r'D:\soft\github1\web_api\test_excel\API.xls')
    da=data.excelApi()
    print(da)