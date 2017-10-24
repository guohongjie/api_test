# #-*-coding:utf-8-*-
import sys
sys.path.append('..')
import data
import unittest
from element.erm_login import Erm_Login
from driver import HTMLTestRunnerCN
import re
import time
from driver.local_ip import re_local_IP
o = Erm_Login()
list_cookies = o.login_erm().items()
str_cookies = str(dict(list_cookies))
apiName = data.api_name() #获取 类 内部变量 ，提取并生成 类:url的 字典,
# 用于进行替换base.py文件内的变量，从而生成UNITTEST_api类
#print apiName
apiCheck = data.api_checkpiont() #读取EXCEL，生成检查点，生成结果以 类:CHECKPIONT 显示
#print apiCheck
suite = unittest.TestSuite() #生成 空 测试集
for api_key,api_value in apiName.items():  #API测试类名:测试数据
    with open('base.py','r') as fileInner:#只读模式打开base模板文件
        Inner = fileInner.read()
        temp_cookies = Inner.replace('{cookies}',str_cookies)
        temp_Inner = temp_cookies.replace('{Object_Name}',api_key) #key替换模板内类名{Object_Name}
        temp_Inner1 = temp_Inner.replace('{Object_Name_CN}',apiCheck[api_key][1])
        temp_Simple = temp_Inner1.replace('{simple_Object_Name}',('test_simple_'+api_key))#如果API步骤为简单的GET,POST，则替换函数名称{simple_Object_Name}
        temp_Mazy = temp_Simple.replace('{mazy_Object_Name}', ('mazy_' + api_key))#如果API步骤比较复杂，则替换{mazy_Object_Name}
        temp_Inner_send_way = temp_Mazy.replace('{send_way}',api_value.pop('send_way')) #api_value删除并返回send_way（发送方式),并替换{send_way}
        temp_Inner_check = temp_Inner_send_way.replace('{request_text}',str(apiCheck[api_key][0]))#EXCEL内获取检查点，并替换{request_text}
        url = api_value.pop('url')#获取API内的URL 链接
        api = ''
        for key,value in api_value.items(): #此时API_VALUE 格式为 POST或 GET 的 数据的LIST
            if key == 'files':
        #判断如果KEY值是上传文件类型的files；
        # PS:获取到的值FILES数据会显示成以下数据，多出：mode 'rb' at 0x02D2D4F0>,故进行加工处理
        # {u'upload_img': {'files': {'field1': ('file.jpg',
        # <open file 'G:\\pycode_api\\data\\w.jpg', mode 'rb' at 0x02D2D4F0>, 'image/jpeg')}}
                s = str(value).replace('<open file ', 'open(r')
                ss = s.replace(' mode ', '')
                pattern = re.compile(' at \w*>')
                result = re.findall(pattern, ss)
                sss = ss.replace(result[0], ')')
                value = sss
            api = "%s%s=%s,"%(api,key,value)#此时API 的值 就是发送的数据值
        #print api
        result = temp_Inner_check.replace('{param}',"""url='%s',%s"""%(url,api))
        #print result
        exec(result.encode('utf-8'))
        txt = """suite.addTests(unittest.TestLoader().loadTestsFromTestCase(%s))"""%(api_key)
        #添加至测试集内
        exec(txt)
#runner = unittest.TextTestRunner()
fp = open(r'G:\py_flask\templates\Api_wc.html','wb')
descriptions = """<strong>测试报告链接地址:(链接浏览时间13:00-14：00)</strong>
<p><font color="#FF0000">%s</font> </p>
<strong>测试执行情况如下:(各功能模块用例条数)</strong><br />
<h5>&nbsp&nbsp&nbsp店铺管理模块：</h5>
    <p><font color="#FF0000">&nbsp  &nbsp  &nbsp  &nbsp &nbsp  1 - 13  </font> </p>
<h5>&nbsp&nbsp&nbsp页面审核：</h5>
<p><font color="#FF0000">&nbsp  &nbsp  &nbsp  &nbsp &nbsp  1 - 02  </font> </p>
<h5>&nbsp&nbsp&nbsp店铺装修：</h5>
<p><font color="#FF0000">&nbsp  &nbsp  &nbsp  &nbsp &nbsp  0 - 00  </font> </p>"""%(re_local_IP())
titles = '测试报告'
runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fp, title=titles,description=descriptions)
#print suite
runner.run(suite)
fp.close()
time.sleep(3)
from driver import ssh_html
hostname = '10.144.24.130'
port = 22
username = 'root'
password = 'root'
local_dir = r'G:\py_flask\templates\Api_wc.html'
remote_dir = r'/Users/a1/Desktop/GUI-report/tempReportFile/test.html'
ssh_html.start_put(hostname,port,username,password,local_dir,remote_dir)
ssh_html.start_cmd(hostname,port,username,password)
from driver import outlook_send
s = outlook_send.OutLookSendMail()

