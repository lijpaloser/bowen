# !/usr/bin/puthon
# # _*_coding:utf_8  _*_
#导入模块
import unittest
from  HTMLTestReportCN import HTMLTestRunner
from  appium  import  webdriver
from  time  import  sleep
import warnings
from  tim.config   import  config_1
from  tim.config  import config_2
class  DS(unittest.TestCase):
    def setUp(self):
        self.des = {
                "device": "android",
                "platformName": "Android",
                "platformVersion": "5.1.1",
                "deviceName": "emulator-5554",
                "appPackage": "com.tencent.mobileqq",
                "appActivity": ".activity.SplashActivity",
                "noReset": "true"
            }
        self.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=self.des)
        sleep(5)
    def test_1(self):
        #点击登录
        self.dr.find_element_by_id('com.tencent.mobileqq:id/btn_login').click()
        #账号密码登录
        for  i  in  config_1.read_data():
            #输入账号
            self.dr.find_element_by_id('请输入QQ号码或手机或邮箱').send_keys(i[0])
            sleep(3.0)
                #输入密码
            self.dr.find_element_by_id('com.tencent.mobileqq:id/password').send_keys(i[1])
            sleep(3.0)
                #点击登录
            self.dr.find_element_by_id('com.tencent.mobileqq:id/login').click()
            sleep(3.0)
            try:
                a = self.dr.find_element_by_id('com.tencent.mobileqq:id/login').text
                self.assertEqual(a,'登 录',msg="登录失败")
                print('登录失败')
            except:
             b =self.dr.find_element_by_id('com.tencent.mobileqq:id/et_search_keyword').text
             self.assertEqual(b,'',msg='断言已经搜索成功')
             print('登录成功')
             sleep(5.0)
    def tearDown(self):
        self.dr.quit()
if __name__ == '__main__':
    # unittest.main()
    config_2.report(test_name=DS('test_1'),report_path=(r'C:\Users\123\PycharmProjects\untitled4\tim\report\a.html'))
