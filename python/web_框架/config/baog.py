# !/usr/bin/puthon
# # _*_coding:utf_8  _*_

from HTMLTestReportCN import HTMLTestRunner
import  unittest

def B_gao(*name,report_path):
    #创建一个测试套件
    # print(chaxun_test)
    suit = unittest.TestSuite()
    # 第二步：向测试套件中添加测试用例《理解成玩具枪弹夹添加bb弹
    # suite.addTest(report_path)
    for i in name[0]:
        print(i)
        suit.addTest(i)
    # 第三步：将生成的测试结果写入HTML文件里，理解成玩具枪上档
    with open(report_path, 'wb')  as   fb:
        runner = HTMLTestRunner(
            stream=fb,
            title="报告的名称",
            description="报告的描述",
            verbosity=2,
            # 输出的内容的详细等级。默认是0 ， 2代表是最详细
        )
        # 执行的测试用例，并生成html测试报告，，，理解成玩具枪发射子弹
        runner.run(suit)