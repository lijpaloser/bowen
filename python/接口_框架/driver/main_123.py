#!/usr/bin/python
# _*_coding:utf-8 _*_
#driver 中主要是控制跑回归测试时只跑哪些模块的用例


from 接口_框架.config.baogao import B_gao


with open(r'C:\Users\123\PycharmProjects\untitled4\接口_框架\data\a.txt','r') as fb:
    a = fb.readlines()
    if 'all' in a :
        B_gao('*')
    else:
        B_gao(a)