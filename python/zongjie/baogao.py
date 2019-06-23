#!/usr/bin/python
#_*_ coding:utf-8 _*_
#unittest    单元测试模块
#生成HTML测试报告
import HTMLTestReportCN
#用于单元测试，验证预期结果与实际结果是否一致，一致代表通过，不一致则代表失败
import  unittest

#unittest.Testcase:代表测试用例
class   T(unittest.TestCase):
    #测试用例方法比喻衣以test开头的
    def test_1(self):
        #预期结果
        x = "宝马"
        #实际结果
        y = "劳斯莱斯"
        #第一个断言方法，判断预期结果与实际结果是否相等
        self.assertEqual(x,y,msg="msg的作用是填写备注信息")
    def test_2(self):
        #预期结果
        x = "宝马"
        #实际结果
        y = "宝马"




if __name__ == '__main__':
     #使用unittest类的main方法，自动加载当前脚本中的类，并自动
    #unittest.main()


    ####################################生成测试报告#######################################
    #第一步创建一个测试套件(文件夹)，理解成玩具枪的弹夹
    suite = unittest.TestSuite()
    #第二步：向测试套件中天街啊测试用例《理解成玩具枪弹夹添加bb弹
    suite.addTest(T('test_1'))
    suite.addTest(T('test_2'))
    #第三步：将生成的测试结果写入HTML文件里，理解成玩具枪上档
    with open ('a.html','wb')  as   fb:
        runner = HTMLTestReportCN.HTMLTestRunner(
        stream = fb,
        title = "报告的名称",
        description = "报告的描述",
        verbosity=2,
        #输出的内容的详细等级。默认是0 ， 2代表是最详细
        )
        #执行的测试用例，并生成html测试报告，，，理解成玩具枪发射子弹
        runner.run(suite)




























