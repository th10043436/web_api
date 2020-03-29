import os
import sys
#下面三行代码可以解决没有模块的报错
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import  unittest
import  logging
from test_case.read_API import readData
import  logging.config

from  test_request.test_re import requ
path11=os.path.dirname(os.path.dirname(__file__))
logging.config.fileConfig(path11+'/test_log/log.conf')
logging = logging.getLogger()


class test_weater(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logging.info('Start')

    @classmethod
    def tearDownClass(cls):
        logging.info('End')


    def setUp(self):
        self.data = readData(r'D:\soft\github1\web_api\test_excel\API.xls')
        self.ex = self.data.excelApi()
        #print(self.ex)

    def test_a(self):
        #print(self.ex[0]['result']['status'],type(self.ex[0]['result']['status']))
        if self.ex[0]['result']['status']==1000:
            tag=True
        self.assertTrue(tag)

    def test_b(self):
        if self.ex[1]['result']['status']==1002:
            tag=True
        self.assertTrue(tag)


if __name__ == '__main__':
    suite=unittest.TestSuite()
    tests=[test_weater('test_a'),test_weater('test_b')]
    suite.addTests(tests)
    runner=unittest.TextTestRunner(verbosity=2)
    runner.run(suite)