#-*-coding:utf-8 -*-
import paramiko,datetime,os
hostname = '10.144.24.130'
port = 22
username = 'root'
password = 'root'
local_dir=r'G:\py_flask\templates\Api_wc..html'
remote_dir=r'/Users/a1/Desktop/GUI-report/tempReportFile/test.html'
def start_put(hostname,port,username,password,local_dir,remote_dir):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, username=username, password=password)
    ftp = ssh.open_sftp()
    ftp.put(local_dir,remote_dir)
    print 'file was upload successful!'
    ftp.close()
def start_cmd(hostname,port,username,password):
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname=hostname, port=port, username=username, password=password)
    stdin, stdout, stderr = s.exec_command(r'python /Users/a1/Desktop/GUI-report/mkdir.py')
    print stdout.read()
    s.close()
