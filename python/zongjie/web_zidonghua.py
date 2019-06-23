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


##定位一组对象
#层级定位：先定位一个大的区域，再从大的区域中定位
#先定位父元素，再定位子元素
#（定位的父元素必须是单个唯一的元素，子元素可以定位一组，也可以定位一个）
# enumerate 两组一一对应


from selenium import webdriver
from  time import  sleep
from  selenium.webdriver.common.action_chains  import ActionChains


# dr = webdriver.Chrome()
# dr.get('https://www.ctrip.com')
# sleep(3)
# ww = dr.find_element_by_id('searchHotelLevelSelect').find_elements_by_tag_name('option')
# print(len(ww))
# for i in ww:
#     if i == '五*':
#         continue
#     else:
#          i.click()#获取某个属性的值
#          sleep(3)



#先定位父元素，再定位子元素
#（定位的父元素必须是单个唯一的元素，子元素可以定位一组，也可以定位一个）
# enumerate 两组一一对应


# dr = webdriver.Chrome()
# dr.get('https://www.jd.com')
# sleep(3)
# ww = dr.find_element_by_xpath('//*[@id="J_cate"]/ul').find_elements_by_class_name('cate_menu_lk')#find_element_by_tag_name('li')
# print(len(ww))
# for i in ww:
#     ActionChains(dr).move_to_element(i).perform()
#     sleep(2)


# dr.switch_to.frame （名称为：iframe内嵌框架）
#作用切换为某一个框架上去
#1.通过ID的值切换：2.通过name的值切换到框架上去：
## 3.先定位框架，再给框架赋值，再运用赋的值

# 例如：

# dr = webdriver.Chrome()
#可以回退到最初的页面上
# dr.switch_to_default_content()
#回退上一个框架上
#dr.switch_to.parent_frame()


# dr = webdriver.Chrome()
# dr.get('https://qzone.qq.com/')
# sleep(3)
# dr.switch_to.frame('login_frame')
# sleep(2)
# dr.find_element_by_id('switcher_plogin').click()
# sleep(2)
# dr.find_element_by_id('u').send_keys('403389348')
# sleep(2)
# dr.find_element_by_id('p').send_keys('li.1998025')
# sleep(3)
# dr.find_element_by_id('login_button').click()
# sleep(3)
# dr.switch_to_frame('tcaptcha_iframe')
# sleep(2)
# wd = dr.find_element_by_xpath('//*[@id="tcaptcha_drag_button"]')
# #drag_and_drop  需要两个参数（起始位置，结束位置）
# #drag_and_drop_by_offset  接受到三个参数（起始位置，X轴左边，Y轴坐标）
# ActionChains(dr).drag_and_drop_by_offset(wd,194,0).perform()



#任何游览器管理窗口的原理
    #1.将每一个窗口用一个特定的字符来标识来标识这个窗口(专业术语为--句柄)
    #       只需要获取到每一个窗口的标识号，通过切换标识号就能达到切换窗口的目的
# dr = webdriver.Chrome()
# dr.get('https://www.douban.com/')
# sleep(3)
# print(dr.title)
# #获取当前窗口标识
# print(dr.current_window_handle)
# sleep(2)
# dr.find_element_by_xpath('//*[@id="anony-nav"]/div[1]/ul/li[1]/a').click()
# sleep(3)
# aa = dr.window_handles
# #切换窗口
# dr.switch_to.window(aa[-1])
# print(dr.title)
# dr.quit()

        #对浏览器滚动条的操作
# dr = webdriver.Chrome()
# dr.get('https://www.douban.com/')
# sleep(3)
# #控制浏览器上的滚动条
# for i in range(0,1000,200):
#     js = "var q=document.documentElement.scrollTop={}".format(i)
#     #执行滚动的动作
#     dr.execute_script(js)
#     sleep(3)



        #对弹出框的操作
# dr = webdriver.Chrome()
# dr.get('file:///C:/Users/123/Desktop/课堂文件/常用文档/abc.html')
# sleep(3)
# dr.find_element_by_xpath('/html/body/input').click()
# sleep(3)
# #切换到弹出框上面去
# ww = dr.switch_to_alert()
# #获取弹出框上面的文本
# print(ww.text)
# #点击确定
# ww.accept()
# #点击取消
# # ww.dismiss()
# #向弹出框输入数据
# ww.send_keys('我是你爸爸，我真伟大')



#智能等待
import selenium.webdriver.support.ui as ui
dr = webdriver.Chrome()
dr.get('https://www.baidu.com')
# sleep(3)    #智能等待
#智能等待
#先创建一个 智能等待的控制器
uniti = ui.WebDriverWait(dr,10)
#如果定位的元素出现了就不必等待了
uniti.until(lambda dr:dr.find_element_by_link_text('hao123').is_displayed())
#检测hao、123这个文本内容是否出现。
#如果出现了执行下面的代码
#如果没出现就一直等待，等待最大为十秒

dr.find_element_by_link_text('新闻').click()











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


# import   unittest
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
