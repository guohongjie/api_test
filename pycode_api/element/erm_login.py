#-*-coding:utf-8 -*-
import requests
import re
class Erm_Login(object):
    """初始登录由于验证码识别率低，这里使用手动增加COOKIES"""
    def getCooikes(self):
        cookies = {'JSESSIONID': 'E2D0AC77ECC5FEBF4078DF6462325D9E'}
        requests.post(url='http://10.115.3.177:3860/bfsShop/list.do',cookies=cookies)
        return cookies
    def login_erm(self):
        headers_lg = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                      'Accept-Encoding': 'gzip, deflate, sdch', 'Accept-Language': 'zh-CN,zh;q=0.8',
                      'Cache-Control': 'max-age=0', 'Connection': 'keep-alive',
                      'Cookie': 'compare=; route=abc3f80556634a3938778755d0ef0e68; erm_stoken=16c81bc1-4900-4f3c-aa9a-4bfdb56b54c3; code_chenk=8cca43be-0f1c-4a59-adf5-71074a8ed346',
                      'Host': 'erm.atguat.com.cn', 'Upgrade-Insecure-Requests': '1',
                      'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}
        url = r'http://erm.atguat.com.cn/'
        s = requests.get(url, headers=headers_lg)
        ss = s.cookies.items()
        erm_token = ss[0][1]

        img_url = r'http://erm.atguat.com.cn/erm/imageCode'
        img = requests.get(img_url)
       # print img.cookies.items()
       # print img.headers

        check_url = r'http://erm.atguat.com.cn/erm/user/checkProtalUser.action'
        check_data = {'userName': 'ermadmin', 'userToken': erm_token}
        r = requests.post(check_url, data=check_data)
       # print r.content
        #print r.cookies.items()

        sub_url = r'http://erm.atguat.com.cn/erm/auth/loginSubmit.action'
        sub_data = {'userName': 'ermadmin',
                    'passWord': '833c2b5e99c43d7e44b1e19e7c52b2cb2525109d32a45c86e2482049acfb643f91be4b5a6d74242371bebb2c428a2178d35556d056fe05aae2f74ea1744441e43a39d407e8771b088f0430f982bd5b554cbbc0f8ca5f6bce5762c37721ef43ea7712ccca4bfdcda959eaa6173b087bae9af7469e1c40ef7ae0e7aee9c91924d2',
                    'passWordSms': '', 'checkCode': '', 'redirectUrl': '', 'mode': 'pwd', 'smsIp': ''}
        headers = {
            'Accept': r'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Connection': 'keep-alive',
            'Content-Length': '336',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': r'JSESSIONID=C362BCF9EA6394507ED91055FFC90951; compare=; route=abc3f80556634a3938778755d0ef0e68; _erm_sso=5db0bc87-4705-4cc8-8068-037fe49b70b2; erm_stoken=%s; code_chenk=da28dc13-8418-4e90-a841-3e63ce8fb022' % (
            erm_token),
            'Host': 'erm.atguat.com.cn',
            'Origin': r'http://erm.atguat.com.cn',
            'Referer': r'http://erm.atguat.com.cn/',
            'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}

        w = requests.post(sub_url, data=sub_data, headers=headers)
        return w.cookies

        # main_url = r'http://erm.atguat.com.cn/main.action'
        # main = requests.get(main_url)
        # return main.cookies

