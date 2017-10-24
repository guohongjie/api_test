#-*-coding:utf-8 -*-
import sys
sys.path.append('..')#添加到PATH
from pycode_api.element.apiConfig import PageObject
from driver.excel import Excel
import collections
def api_name():
    """返回类变量用于API接口测试"""
    api_list = Excel(r'G:\pycode_api\data\api.xlsx','api').next()#读取API.XLSX 文件内容
    txt ="""def getAttrbute(str_class):
    exec(str_class)
    dict_module = dict(PageObject.{API_NAME}.__dict__)
    list =['__module__','__dict__','__weakref__','__doc__']
    for m in list:
        dict_module.pop(m)
    return dict_module
        """#定义获取类变量数据
    api = collections.OrderedDict() #生成一个有序空字典，避免unittest.testsuite按照ASICC码大小顺序执行
    #print api_list
    for m in api_list:
        new_txt = txt.replace('{API_NAME}',m[u'API_NAME'])
        #print new_txt
        exec(new_txt)
        api[m[u'API_NAME']] = getAttrbute('PageObject') #将API数据添加至api变量
    return api
def api_checkpiont():
    """返回类:CHECKPIONT"""
    a = Excel(r'G:\pycode_api\data\api.xlsx', 'api')
    s = a.next()
    n = {}
    for m in s:
        h = m.pop(u'API_NAME')
        n[h] = [m.pop(u'CHECKPOINT'),m.pop(u'API_CN_NAME')]
    return n
if __name__ == "__main__":
    print api_checkpiont()
