# !/usr/bin/puthon
# # _*_coding:utf_8  _*_

import xlrd
def shuju():
    he = []
    f = xlrd.open_workbook(r'C:\Users\123\PycharmProjects\untitled4\接口_框架\data\suopei.xlsx')
    sheet = f.sheets()[0]
    for i in range(sheet.nrows):
        he.append(sheet.row_values(i))
    return he
if __name__ == '__main__':
   print(shuju())