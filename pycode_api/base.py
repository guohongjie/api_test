#-*-coding:utf8 -*-
import unittest
import requests
#from element.erm_login import test_login
import re
class {Object_Name}(unittest.TestCase):
    """接口- {Object_Name_CN} -测试"""
    def setUp(self):
        self.send_way = '{send_way}'
        #self.login = test_login()
        self.cookies = {cookies}
    def {simple_Object_Name}(self):
       # """接口测试  {Object_Name}"""
        with requests.{send_way}({param}cookies=self.cookies) as r:
            self.__assert('{request_text}', r.content)
            if r.status_code == 200:
                print r.content
    def {mazy_Object_Name}(self):
        pass
        # """Test mazy  {Object_Name}"""
        # with requests.{send_way}({param}cookies=self.cookies) as r:
        #     self.__assert('{request_text}', r.content)
        #     if r.status_code == 200:
        #         print r.content
    def __assert(self, request, response):
        pattern = re.compile(request)
        list_re = re.findall(pattern, response)
        self.assertIn(request, list_re, msg='Request and Response is not equal!!!\n %s \n %s'%(request,response))
    def tearDown(self):
        pass
