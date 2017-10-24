#-*-coding:utf-8 -*-
TEMPLATE = """<?xml version="1.0" encoding="UTF-8"?>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>   <title>测试报告</title>
    <meta name="generator" content="HTMLTestRunner 0.8.2.1"/>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    <link href="http://libs.baidu.com/bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet">
    <script src="http://libs.baidu.com/jquery/2.0.0/jquery.min.js"></script>
    <script src="http://libs.baidu.com/bootstrap/3.0.3/js/bootstrap.min.js"></script> 
<style type="text/css" media="screen">
body        { font-family: Microsoft YaHei,Tahoma,arial,helvetica,sans-serif;padding: 20px; font-size: 80%%; }
table       { font-size: 100%%; }
/* -- heading ---------------------------------------------------------------------- */
.heading {
    margin-top: 0ex;
    margin-bottom: 1ex;
}

.heading .description {
    margin-top: 4ex;
    margin-bottom: 6ex;
}
/* -- report ------------------------------------------------------------------------ */
#total_row  { font-weight: bold; }
.passCase   { color: #5cb85c; }
.failCase   { color: #d9534f; font-weight: bold; }
.errorCase  { color: #f0ad4e; font-weight: bold; }
.hiddenRow  { display: none; }
.testcase   { margin-left: 2em; }
</style>
</head>
<body >
<div class='heading'>
<h1 style="font-family: Microsoft YaHei">测试报告</h1>
<p class='attribute'><strong>测试人员 : </strong> 帅气的测试组 </p>
<p class='attribute'><strong>开始时间 : </strong> %s </p>
<!--p class='attribute'><strong>合计耗时 : </strong> 0:00:16.196000</p-->
<p class='attribute'><strong>测试结果 : </strong> 共 %s，通过 %s，通过率= %s</p>
<!--p class='description'><strong>测试报告链接地址:(链接浏览时间13:00-14：00)</strong>
<p><font color="#FF0000">10.144.33.191:80</font> </p-->
<strong>测试执行情况如下:(各功能模块用例条数)</strong><br />
	<p> %s </p>
<p id='show_detail_line'>
<a class="btn btn-primary">概要{ 100.00%% }</a>
<a class="btn btn-danger">失败{ %s }</a>
<a class="btn btn-success">通过{ %s }</a>
	<a class="btn btn-success">跳过{ %s }</a>
<a class="btn btn-info">所有{ %s }</a>
</p>
<table id='result_table' class="table table-condensed table-bordered table-hover">
<colgroup>
<col align='left' />
<col align='right' />
<col align='right' />
<col align='right' />
<col align='right' />
<col align='right' />
</colgroup>
<tr id='header_row' class="text-center success" style="font-weight: bold;font-size: 14px;">
    <td>用例集/测试用例</td>
    <td>总计</td>
    <td>通过</td>
    <td>失败</td>
    <td>详细</td>
</tr>
%s
%s
</tr>
</table>
<div id='ending'>&nbsp;</div>
    <div style=" position:fixed;right:50px; bottom:30px; width:20px; height:20px;cursor:pointer">
    <a href="#"><span class="glyphicon glyphicon-eject" style = "font-size:30px;" aria-hidden="true">
    </span></a></div>
</div>
</body>
</html>
"""
TEMPCASESUITE = """<tr class='passClass warning'>
    <td> %s </td>
    <td class="text-center">1</td>
    <td class="text-center">%s</td>
    <td class="text-center">%s</td>
    <td class="text-center">%s</td>
</tr>
"""
TOTAL = """
<tr id='total_row' class="text-center active">
    <td>总计</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>通过率：%s</td>
    """
