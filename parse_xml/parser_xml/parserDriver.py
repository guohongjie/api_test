#-*-coding:utf-8 -*-
from bs4 import BeautifulSoup
from html_template import template
class ParseXmlUseBS(object):
    def parseXml(self,path):
        soup = BeautifulSoup(open(path),'html.parser')
        #test soup.testsuite.get("timestamp")
        testdate = soup.testsuite.get("timestamp") #测试日期
        testsuiteCount = soup.testsuite.get('tests') #用例条数
        report_feature = soup.testcase.get('classname') #抓取测试场景描述
        count = 0#计数器
        content = ''
        for singleCase in soup.find_all('testcase'):
            soup1 = BeautifulSoup(str(singleCase),'html.parser')
            if 'failure' in str(soup1):
                error_msg = soup1.find('failure')
                content = "%s\n%s"%(content,error_msg)
                #content = str(count)+":"+content+'\n %s'%(error_msg)
                break
            else:
                content = "%s\n%s"%(content,(singleCase.get('name')))#获取测试步骤
                count = count+1
        testCase = content #测试用例
        passCount = count # pass 数量
        if int(testsuiteCount)-int(count)-1>0:#跳过执行的数据
            skipped=int(testsuiteCount)-int(count)-1
        else:
            skipped=0
        if int(passCount)==int(testsuiteCount):
            failure = 0
        else:
            failure = 1
        #print skipped
        dict_report_element = {u'测试日期':testdate,u'测试用例条数':testsuiteCount,'Pass':passCount,
            u'测试执行用例':testCase,'Failure':failure,'Skipped':skipped,'Feature':report_feature}
        return dict_report_element

if __name__ == "__main__":
    a = ParseXmlUseBS()
    data = a.parseXml()
    list_report = []
    list_testCastSuite = [x for x in data[u'测试执行用例'].split('\n') if x]
    passPerson = '%.2f%%' % (float(data[u'Pass']) / float(data[u'测试用例条数']) * 100)
    a, b, c, d, e, f, g, h = data[u'测试日期'], data[u'测试用例条数'], data['Pass'], passPerson, data['Feature'], data['Pass'],data['Skipped'], data[u'测试用例条数']
    for m in list_testCastSuite:
        if 'failure' in m:
            report1 = template.TEMPCASESUITE%(str(m).lstrip('<').rstrip('>'),'0','1','测试未通过')
            #print report1
            list_report.append(report1)
            break
        report = template.TEMPCASESUITE%(str(m),'1','0','步骤操作通过')
        list_report.append(report)
   # print list_report
    report = ''.join(list_report)
    total = template.TOTAL%(str(b),str(c),'1',str(passPerson))
    s = template.TEMPLATE%(str(a),str(b),str(c),str(d),str(e),str(f),str(g),str(h),str(report),str(total))
    with open(r'C:\Users\guohongjie\Desktop\wc.html','w') as f:
        f.write(s)
