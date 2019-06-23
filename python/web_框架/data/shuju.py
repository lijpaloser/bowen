#!/bin/python
# __*__ coding:utf-8


def shuju():
    he = []
    with open(r'C:\Users\123\PycharmProjects\untitled4\web_框架\data\data_1.txt','r',encoding='utf-8') as f:
        a = f.readlines()
        for i in a:
            he.append(a)
        return he
shuju()