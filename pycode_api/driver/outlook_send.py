# -*- coding:utf-8 -*-
import win32com.client as win32
#import warnings
import sys
import time
reload(sys)
sys.setdefaultencoding('utf8')
#warnings.filterwarnings('ignore') 忽略警告提示
class OutLookSendMail(object):
    def __init__(self):
        times = time.asctime( time.localtime(time.time()) )
        files = open(r'G:\py_flask\templates\Api_wc.html','rb').read()
        temp_files = files.replace(r'<pre',r'<!--pre"')
        temp_files1 = temp_files.replace(r'详细','')
        new_files = temp_files1.replace(r'/pre>','/pre-->')
        self.sendemail(u'%s接口测试报告'%(times),new_files)
        print 'Email was send successful!!'
        # s = open(r'.\t.html','w')
        # s.write(new_files)
        # s.close()
    def sendemail(self,sub,body):
        outlook = win32.Dispatch('outlook.application')
        receivers = ['guohongjie@gomeplus.com;wuzhou-ds@gomeplus.com;zhangweixi-ds@gomeplus.com']
        mail = outlook.CreateItem(0)
        mail.To = receivers[0]
        mail.Subject = sub.decode('utf-8')
        mail.HTMLBody = body.decode('utf-8')
        # 添加附件
        mail.Attachments.Add(r'G:\py_flask\templates\Api_wc.html')
        mail.Send()
if __name__ == "__main__":
    a = OutLookSendMail()
