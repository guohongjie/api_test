#-*-coding:utf-8 -*-
import unittest
import ddt
@ddt.ddt
class MyTestCase(unittest.TestCase):
    def setUp(self):
        print 'setup'
    @ddt.data([{1:'a'},'b'],[{2:'b'},'c'])
    @ddt.unpack
    def test_something(self,testdata,expectedresult):
        print "test something"
        print testdata
        print expectedresult
    def tearDown(self):
        print 'tearDown'

if __name__ == "__main__":
    unittest.main()