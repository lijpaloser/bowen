#!/usr/bin/python
# _*_coding:utf-8 _*_
from HTMLTestReportCN import HTMLTestRunner
import  unittest

def B_gao(name):
    #创建一个测试套件
    suit = unittest.TestSuite()
    #将测试用例添加到测试套件里
    #讲某一个类中所有的测试用例
    # suit.addTest(unittest.makeSuite('类名'))
    #需要两个参数：第一个是存放测试脚本的路径，
    # #第二个参数是匹配测试文件的通配符语句
    #可以自动发现符合通配符的文件中以test开头的函数，提取出来放在discover列表中
    for i in name:
        dis = unittest.defaultTestLoader.discover(r'C:\Users\123\PycharmProjects\untitled4\接口_框架\test\_test',pattern='{}_test.py'.format(i.strip()))
        for i in dis:
            suit.addTest(i)
        f = open(r'C:\Users\123\PycharmProjects\untitled4\接口_框架\report\aa.html','wb',)
        runner =HTMLTestRunner(
            stream = f,
            title = '别克测试报告',
            description = '报告的描述',
            verbosity = 2)
        runner.run(suit)
        f.close()
if __name__ == '__mian':
         B_gao('*')