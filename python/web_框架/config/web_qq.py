#!/usr/bin/python
# __*__ coding:utf-8 __*__
from selenium  import webdriver
from time import sleep
from  selenium.webdriver.common.action_chains  import ActionChains


dr = webdriver.Firefox()
dr.get('https://shurufa.baidu.com/skin_list')
sleep(3)
# dr.switch_to.frame('login_frame')
# sleep(2)
dr.find_element_by_link_text('皮肤').click()
sleep(2)
dr.find_element_by_id('keyword').click()
sleep(2)
a = ['王者','穿越','阴阳师','炫舞','三大发顺丰无人','dajijtrkjaoimklm']
for i in a:
    dr.find_element_by_xpath('//*[@id="keyword"]').send_keys(i)
    sleep(2)
    dr.find_element_by_class_name('submit').click()
    try:
        dr.find_element_by_link_text('最新')
        print('pass')
    except:
        bb = dr.find_element_by_class_name('face')
        print('pass')
        # return cha_xun()



