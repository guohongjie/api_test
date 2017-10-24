#-*-coding:utf-8 -*-
import ssh_html
import time
hostname = '10.144.24.130'
port = 22
username = 'root'
password = 'root'
local_dir=r'G:\py_flask\templates\Gui_wc.html'
remote_dir=r'/Users/a1/Desktop/GUI-report/tempReportFile/test.html'
ssh_html.start_put(hostname,port,username,password,local_dir,remote_dir)
ssh_html.start_cmd(hostname,port,username,password)
print 'ssh was ok'

import outlook_send
outlook_send.OutLookSendMail()
time.sleep(2)
print 'sendMail was ok'
