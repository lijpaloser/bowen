# !/usr/bin/puthon
# # _*_coding:utf_8  _*_

#定义一个读取txt文件的函数
def read_data():
    datas = []
    with open(r'C:\Users\123\PycharmProjects\untitled4\tim\data\data_1','r')  as b :
        d  =  b.readlines()
        for i in d :
          datas.append(i.replace('\n','').split(','))
          # print(i.replace('\n', '').split(','))
        return  datas
print(read_data())
# read_data()