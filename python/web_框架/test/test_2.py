# !/usr/bin/puthon
# # _*_coding:utf_8  _*_
# from web_框架.config.config_1 import qing_qiu
import unittest
from HTMLTestReportCN import HTMLTestRunner
from web_框架.config.baog import B_gao
from  web_框架.data import shuju
from selenium import webdriver
from  time import sleep

class duan_yan(unittest.TestCase):
    def duan(self):
        dr = webdriver.Firefox()
        dr.get('https://shurufa.baidu.com/skin_list')
        sleep(3)
        # dr.switch_to.frame('login_frame')
        # sleep(2)
        dr.find_element_by_link_text('皮肤').click()
        sleep(2)
        dr.find_element_by_id('keyword').click()
        sleep(2)
        a = shuju.shuju()
        for i in a:
            dr.find_element_by_xpath('//*[@id="keyword"]').send_keys(i)
            sleep(2)
            dr.find_element_by_class_name('submit').click()

            # try:
            #     dr.find_element_by_link_text('最新')
            #     print('pass')
            # except:
            #     bb = dr.find_element_by_class_name('face')
            #     print('pass')

    def test1(self):
        dr = webdriver.Firefox()
        # log.info('登录成功测处理')
        b = dr.find_element_by_link_text('最新')
        print("pass")
        self.assertEqual(b, "最热", msg="断言失败")
    def test2(self):
            # 断言
        dr = webdriver.Firefox()
        a = dr.find_element_by_link_text('没有找到相应结果，换个关键词试试吧')
        self.assertEqual(a,'没有找到相应结果，换个关键词试试吧',msg="断言成功")
        print("pass")
if __name__ == '__main__':
    B_gao(duan_yan('test1'),duan_yan('test2'),report_path=r'C:\Users\123\PycharmProjects\untitled4\web_框架\report\b.html')