#-*- coding:utf-8 -*-
import xlrd
class Excel(object):
    def __init__(self, excelPath, sheetName):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)
        self.row = self.table.row_values(0)
        self.rowNum = self.table.nrows
        self.colNum = self.table.ncols
        self.curRowNo = 1
    def next(self):
        r = []
        while self.hasNext():
            s = {}
            col = self.table.row_values(self.curRowNo)
            i = self.colNum
            for x in range(i):
                s[self.row[x]] = col[x]
            r.append(s)
            self.curRowNo += 1
        return r
    def hasNext(self):
        boolen = False if self.rowNum == 0 or self.rowNum <= self.curRowNo else True
        return boolen
if __name__ == "__main__":
    a = Excel(r'G:\pycode_api\data\api.xlsx','api')
    s = a.next()
    n ={}
    for m in s:
        h = m.pop(u'API_NAME')
        n[h]=m.pop(u'CHECKPOINT')
    print n
