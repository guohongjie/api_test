#-*-coding:utf-8 -*-
import socket
def re_local_IP():
    localIP = socket.gethostbyname(socket.gethostname())#得到本地ip
    return '%s:80'%localIP
#print re_local_IP()
