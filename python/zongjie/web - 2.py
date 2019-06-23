#!/usr/bin/python
#安装selenium模块
#wed 自动化
# Python  代码，控制浏览器打开网页
# #驱动，不同的浏览器对应不同的驱动
# # from  selenium import webdriver
# # #打开浏览器
# # from   time import sleep
# # dr = webdriver.Chrome()
# # # #请求要打开的网页
# # dr.get('https://www.baidu.com')
# # sleep(2)
# # #打印打开的网页标题
# # # print(dr.title)
# # if dr.title == '百度一下，你就知道':
# #     print('yes')
# #     # \
# # #打印当前的网址
# # # print(dr.current_url)
# # #设置浏览器窗口大小
# # dr.set_window_size(400,400)
# # #设置浏览器的位置
# # dr.set_window_position(400,400)
# # #最大化浏览器窗口
# # dr.maximize_window()
# # #最小化浏览器窗口
# # dr.minimize_window()
# # #回退
# # dr.get('https://www.baidu.com')
# # sleep(2)
# # dr.get('https://jd.com')
# # sleep(2)
# # dr.back()
# # #前进
# # sleep(2)
# # dr.forward()
# # #1   最重要：id定位    动作：   send_keys  输入   click  点击
# ##2...通过name属性进行定位
# ##  3 ...class  属性定位
# #   4 ....link_text 根据文本定位
# #    5.。。。partial_link_text
# #   6.....tag_name  根据标签的名称来定位
# #   7.....xpath   根据路径标记   路径标记语言
# #    //*[@id="u_sp"]/a[2]        相对路径
# #   8.....css_selector         根据css定位
# #
# #  无论采用任何方式的定位，一定要保证定位的唯一性
# #
# #
# # dr.find_element_by_id('kw').send_keys('python')
# # sleep(2)
# # dr.find_element_by_id('su').click()
# # sleep(5)
# # dr.find_element_by_class_name('').send_keys('python')
# # sleep(2)
# # dr.find_element_by_link_text('hao123').click()
# # dr.find_element_by_css_selector('#u_sp > a:nth-child(2)').click()
#
# #登录QQ空间
# from  selenium import webdriver
# from   time import sleep
# dr = webdriver.Chrome()
# dr.get('https://qzone.qq.com')
# sleep(2)
# dr.switch_to.frame('login_frame')
# sleep(2)
# dr.find_element_by_id('switcher_plogin').click()
# sleep(2)
# dr.find_element_by_id('u').send_keys('1403380397')
# sleep(2)
# dr.find_element_by_id('p').send_keys('li.19980325')
# sleep(2)
# dr.find_element_by_id('login_button').click()


# 登录QQ邮箱
# from  selenium import webdriver
# from   time import sleep
# dr = webdriver.Chrome()
# dr.get('https://mail.qq.com')
# sleep(3)
# dr.switch_to.frame('login_frame')
# sleep(3)
# dr.find_element_by_xpath('//*[@id="1"]/h3/a[1]/em').click()
# sleep(3)
# dr.find_element_by_id('switcher_plogin').click()
# sleep(3)
# dr.find_element_by_class_name('inputstyle').send_keys('1403380397')
# sleep(3)
# dr.find_element_by_class_name('inputstyle  password').send_keys('li.19980325')
# sleep(3)
# dr.find_element_by_xpath('//*[@id="login_button"]').click()


import   unittest
#unittest写单元测试用的，写断言用
#预期结果与实际结果作比对的过程
# class duanyan(unittest.TestCase):
#     def test_1(self):
#         #假设预期结果是1，实际结果是2，判断预期结果是否等于实际结果
#         a = 1 #预期结果
#             #断言
#         self.assertEqual(a ,2)
#
# # if __name__ == '__main__':
# #         unittest.main()
#
#
# from appium import webdriver
# from time import sleep
#
#
# # 面向对象
# class Tim(object):
#
#     # 初始化属性
#     def __init__(self):
#         # 建立与appium服务器需要的参数，以字典的形式
#         self.des = {
#             "device": "android",
#             "platformName": "Android",
#             "platformVersion": "9",
#             "deviceName": "46HDU19314003325",
#             "appPackage": "com.tencent.tim",
#             "appActivity": "com.tencent.mobileqq.activity.SplashActivity",
#             "noReset": "true",
#         }
#         # http://127.0.0.1:4723/wd/hub 固定的，写死localhost==127.0.0.1
#         # 测试脚本与appium服务器建立一个session连接
#         self.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=self.des)
#         sleep(5)
#
#     def dian_zan(self):
#         # 第一步，点击办公
#         self.dr.find_element_by_id('android:id/tabs').find_elements_by_class_name('android.widget.RelativeLayout')[
#             -1].click()
#         # 第二步，点击好友动态
#         t = self.dr.find_element_by_id('com.tencent.tim:id/lebasv').find_elements_by_class_name(
#             'android.widget.RelativeLayout')
#         t[-1].click()
#         sleep(0.5)
#         # 第三步 点赞
#         x = self.dr.find_elements_by_class_name('android.widget.ImageView')
#         print(x)
#         x[1].click()
#         sleep(2)
#         x[2].click()
#

# 调用类
# if __name__ == '__main__':
#     yasuo = Tim()
#     yasuo.dian_zan()








#web自动化

# selenium:web自动化测试工具集
#selenium 特点：
        #1. 开源，免费
        #2.多浏览器支持。firefox，Chrome，IE，Opera，Safari
        #3.多平台支持
        #selenium1.0的组成（1.0 , 2.0 , 3.0）
# 1. selenium ： IDE 是火狐浏览器的一个插件
#       作用:录制和回放
#2.  selenium  Grid：是自动化测试的一个辅助工具
#       作用：可以实现在不同的环境中同时执行测试
#3.  selenium Rc： selenium1.0是自动化测试的核心
#       作用：控制浏览器的行为

        #selenium2.0的组成
#1.  selenium1.0内所有的工具（selenium IDE / Grid / Rc）+ webdriver
# 2. webdriver  是selenium2.0的核心
#       作用：控制浏览器的行为

# 区别
# selenium Rc       ：通过将测试代码转换成javaScript能够识别的动作，从而间接的控制浏览器
#selenium webdriver ：通过将浏览器的所有的原生接口集成到webdriver驱动中，然后通过驱动直接控制流浏览器
#下载的驱动解压是一个程序 .exe 软件

#自动登录QQ空间
# from selenium import webdriver
# from  time import  sleep
#
# dr = webdriver.Chrome()
# sleep(2)
# dr.get('http://qzone.qq.com')
# sleep(2)
# dr.switch_to.frame('login_frame')
# sleep(2)
# dr.find_element_by_id('switcher_plogin').click()
# sleep(2)
# dr.find_element_by_id('u').send_keys('1403380397')
# sleep(2)
# dr.find_element_by_id('p').send_keys('li.19980325')
# sleep(2)
# dr .find_element_by_id('login_button').click()
# sleep(2)
