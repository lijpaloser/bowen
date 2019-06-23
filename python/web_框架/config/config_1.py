#!/usr/bin/python
# __*__ coding:utf-8 __*__

from selenium  import webdriver
from time import sleep
# import web_框架.data



def qing_qiu():
    dr = webdriver.Firefox()
    dr.get('https://shurufa.baidu.com/skin_list')
    sleep(3)
    # dr.switch_to.frame('login_frame')
    # sleep(2)
    dr.find_element_by_link_text('皮肤').click()
    sleep(2)
    dr.find_element_by_id('keyword').click()
    sleep(2)