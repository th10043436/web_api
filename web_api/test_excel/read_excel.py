import  xlrd
class readEx(object):
    def __init__(self,path_01):
        self.data = xlrd.open_workbook(path_01)
        self.table = self.data.sheet_by_name('Sheet1')
        # 获取总行数
        #print('总行数 %d' % self.table.nrows)
        # 获取总列数
        #print('总列数 %d' % self.table.ncols)

    def read_ex(self):
        list = []
        # 获取第一行
        key = self.table.row_values(0)
        # print(key)
        for i in range(self.table.nrows - 1):
            print(i)
            dict = {}
            # 获取第二行数据
            cells = self.table.row_values(i + 1)
            #print(cells)
            for j in range(len(cells)):
                dict[key[j]] = cells[j]
            list.append(dict)
        return list

if __name__ == '__main__':
    ex=readEx(r'D:\soft\github1\web_api\test_excel\API.xls')
    list=ex.read_ex()
    #print(list)

    #print(type(eval(list[0]['参数'])))#str转为为字典