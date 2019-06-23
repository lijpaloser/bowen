# !/usr/bin/puthon
# # _*_coding:utf_8  _*_
#导入模块
from HTMLTestReportCN import HTMLTestRunner
from selenium import webdriver
import unittest
from appium import webdriver
from time import sleep
import warnings
from deisheng.config import config_1
from  deisheng.config  import  config_2
#导入封装好的日至函数
from  deisheng.config.config_3 import  get_logger
#创建变量接受日志的句柄
log = get_logger('test_1')
#log.info('想要打印出来的内容')



class DS(unittest.TestCase):
    '''
        def __init__(self):-->初始化函数，传递参数，自动运行
    '''

    # 每个用例执行之前运行一次，作用：用于清理测试环境残留数据，初始化测试环境
    def setUp(self):      #相当于init方法，类被调用的时候，会自动运行
        warnings.simplefilter('ignore', ResourceWarning)
        self.des = {
            "device": "android",
            "platformName": "Android",
            "platformVersion": "5.1",
            "deviceName": "4H7SZSDA6SR8BUAQ",
            "appPackage": "com.qk.butterfly",
            "appActivity": ".main.LauncherActivity",
            "noReset": "true",
        }
        # http://127.0.0.1:4723/wd/hub 固定的，写死localhost==127.0.0.1
        # 测试脚本与appium服务器建立一个session连接
        self.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=self.des)
        sleep(5.0)
        log.info('手机与appium服务器建立链接完成')
    # 写测试用例的部分
    def test_1(self):
        # 使用账号密码登录蝶声
        # 点击密码，进入手机号、密码登录页面
        log.info('点击密码按键，进入账号密码登陆页面')
        self.dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').click()
        # 进入账号密码登录页面之后
        for i in config_1.read_data():
            self.dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys(i[0])
            log.info(f'输入的手机号是：{i[0]}')
            self.dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').send_keys(i[1])
            log.info(f'输入的手机号是：{i[1]}')
            self.dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').click()
            log.info(f'点击登录按钮')

        # 断言
            sleep(5.0)
            """
            if else  处理登陆成功与失败，也可以用try  excep。t 语句做断言
            """
            try:
                # 登录失败，还在登录界面
                log.info('登录成功测处理')
                b = self.dr.find_elements_by_id('').text
                print("登录失败")
                self.assertEqual(b, "登录", msg="登录失败")
            except:
                # 断言
                sleep(5.0)
                # 进入登录之后的页面
                a = self.dr.find_elements_by_id('')[-1].text
                self.assertEqual(a, '我的', msg="断言已经登陆成功")
                print("登录成功")
        # 每个测试用例执行完毕之后，运行teardown一次，作用：测试用例运行完，清理测试环境

    def tearDown(self):
        log.info('手机与appium断开连接')
        self.dr.quit()


if __name__ == '__main__':
    # unittest.main()
    config_2.report(test_name =DS('test_1'),report_path=r'C:\Users\123\PycharmProjects\untitled4\deisheng\report\a.html')