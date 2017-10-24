#-*-coding:utf-8 -*-
from html_template import template
from parser_xml import parserDriver
class MakeHTML(object):
    def return_HTML(self):
        a = parserDriver.ParseXmlUseBS()
        data = a.parseXml(r'G:\pycode_BDD\Test_BDD\lettucetests.xml')
        list_report = []
        list_testCastSuite = [x for x in data[u'测试执行用例'].split('\n') if x]
        passPerson = '%.2f%%' % (float(data[u'Pass']) / float(data[u'测试用例条数']) * 100)
        a, b, c, d, e, f, g, h,Failure = data[u'测试日期'], data[u'测试用例条数'], data['Pass'], passPerson, data['Feature'], data[
            'Pass'], data['Skipped'], data[u'测试用例条数'],data['Failure']
        for m in list_testCastSuite:
            if 'failure' in m:
                report1 = template.TEMPCASESUITE % (str(m).lstrip('<').rstrip('>'), '0', '1', '测试未通过')
                # print report1
                list_report.append(report1)
                break
            report = template.TEMPCASESUITE % (str(m), '1', '0', '步骤操作通过')
            list_report.append(report)
            # print list_report
        report = ''.join(list_report)
        if int(b)==int(c):
            total = template.TOTAL % (str(b), str(c), 0, str(passPerson))
        else:
            total = template.TOTAL % (str(b), str(c), 1, str(passPerson))
        s = template.TEMPLATE % (
        str(a), str(b), str(c), str(d), str(e),str(Failure), str(f), str(g), str(h), str(report), str(total))
        with open(r'G:\py_flask\templates\Gui_wc.html', 'w') as f:
            f.write(s)
if __name__ == "__main__":
    a = MakeHTML()
    a.return_HTML()
