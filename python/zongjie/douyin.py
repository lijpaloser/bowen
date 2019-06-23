#!/usr/bin/python
#_*_ coding:utf-8 _*_
from appium import  webdriver
from time   import  sleep
# 模拟器抖音
# des = {
#     "platformName": "Android",
#     "platformVersion": "5.1.1",
#     "deviceName": "emulator-5554",
#     "appPackage": "com.ss.android.ugc.aweme",
#     "appActivity": ".main.MainActivity",
#     "noReset": "true"
#         }
# # 'http://127.0.0.1:4723/wd/hub', desired_capabilities=de  固定的，写死  localhost=127.0.0.1
# # 测试脚本与appium服务器建立一个session链接
# #
# dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=des)
# sleep(12)
# # 第一步：先定义一个元素
# # 第二步：再定位多个元素
# items = dr.find_element_by_id('com.ss.android.ugc.aweme:id/ca9').find_elements_by_class_name('android.widget.FrameLayout')
# sleep(2)
# print(items)
# sleep(12)
# #退出app
# dr.quit()


# 模拟器TIM
# des ={
#       "platformName": "Android",
#       "platformVersion": "5.1.1",
#       "deviceName": "emulator-5554",
#       "appPackage": " com.tencent.tim",
#       "appActivity": "com.tencent.mobileqq.activity.SplashActivity",
#       "noReset": "true"
#     }
# dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=des)
# sleep(2)
# dr.find_element_by_accessibility_id('请输入QQ号码或手机或邮箱').clear()
# dr.find_element_by_accessibility_id('请输入QQ号码或手机或邮箱').send_keys('1417926350')
#
# dr.find_element_by_id('com.tencent.tim:id/password').send_keys('hwl1997521.')
#
# dr.find_element_by_id('com.tencent.tim:id/login').click()
# sleep(2)
#滑动操作
#第一步：获取手机屏幕大小

# s = dr.get_window_size()
# #第二步：放缩x，y
# x1 = s['width'] * 0.5
# y1 = s['height'] * 0.25
# y2 = s['height'] * 0.75
# dr.swipe(x1,y1, x1,y2)
# sleep(5)
# dr.quit()



# items = dr.find_element_by_id('android:id/tabs').find_elements_by_class_name('android.widget.RelativeLayout')
# sleep(2)
# print(items)
# for i in items:
#     sleep(0.5)
#     i.click()
#     sleep(0.5)
#
# dr.quit()

#评论空间说说
#第一步：点击办公
# dr.find_element_by_id('android:id/tabs').find_elements_by_class_name('android.widget.RelativeLayout')[2].click()
# #第二步：点击好友状态
# dr.find_element_by_accessibility_id('好友动态').click()
# dr.find_elements_by_id('com.tencent.tim:id/Leb')
# sleep(3)
# t = dr.find_elements_by_class_name('android.widget.ImageView')
# print(t)
# t[1].click()
# sleep(2)
# t[2].click()
# dr.quit()

#dr.find_elements_by_id('com.tencent.tim:id/main').find__elements_by_class_name('android.widget.ImageView')



#面向对象
#TIM

# class Tim(object):
#     #初始化属性
#     def __int__(self):
#         des = {
#               "platformName": "Android",
#               "platformVersion": "5.1.1",
#               "deviceName": "emulator-5554",
#               "appPackage": " com.tencent.tim",
#               "appActivity": "com.tencent.mobileqq.activity.SplashActivity",
#               "noReset": "true"
#             }
#         #建立连接
#         self.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=des)
#         sleep(2)
#     def dian_zan(self):
#         self.dr.find_element_by_id('android:id/tabs').find_elements_by_class_name('android.widget.RelativeLayout')[2].click()
#         #第二步：点击好友状态
#         x = self.dr.find_element_by_id('com.tencent.tim:id/lebasv').find_elements_by_class_name('android.widget.RelativeLayout')
#         x[-1].click()
#         sleep(0.5)
#         t = self.dr.find_elements_by_class_name('android.widget.ImageView')
#         print(t)
#         t[1].click()
#         sleep(2)
#         t[2].click()
# 面向对象






class Tim(object):

    # 初始化属性
    def __init__(self):
        # 建立与appium服务器需要的参数，以字典的形式
        self.des = {
            "platformName": "Android",
            "platformVersion": "5.1.1",
            "deviceName": "emulator-5554",
            "appPackage": "com.tencent.tim",
            "appActivity": "com.tencent.mobileqq.activity.SplashActivity",
            "noReset": "true",
        }
        # http://127.0.0.1:4723/wd/hub 固定的，写死localhost==127.0.0.1
        # 测试脚本与appium服务器建立一个session连接
        self.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=self.des)
        sleep(5)

    def dian_zan(self):
        # 第一步，点击办公
        self.dr.find_element_by_id('android:id/tabs').find_elements_by_class_name('android.widget.RelativeLayout')[-1].click()
        # 第二步，点击好友动态
        t = self.dr.find_element_by_id('com.tencent.tim:id/lebasv').find_elements_by_class_name('android.widget.RelativeLayout')
        t[-1].click()
        sleep(0.5)
        # 第三步 点赞
        x = self.dr.find_elements_by_class_name('android.widget.ImageView')
        print(x)
        x[1].click()
        sleep(2)
        x[2].click()

        # 获取文字
    def get_wenzi(self):
        a = self.dr.find_element_by_id('com.tencent.tim:id/ivTitleName').text
        print(a)
        return a
    def anjian(self):
        #模拟人点击物理按键操作
        #点击home键
        self.dr.keyevent(3)
        #点击返回键



#调用类
if __name__ == '__main__':
    yasuo = Tim()
    #yasuo.dian_zan()
    #yasuo.get_wenzi()
    yasuo.anjian()


































