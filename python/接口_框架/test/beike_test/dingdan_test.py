# !/usr/bin/puthon
# # _*_coding:utf_8  _*_
from 接口_框架.config.chaxun import Cha_xun
from  接口_框架.data.duqu_dingdan import shuju
import unittest
class D_dan(unittest.TestCase):
    ss = shuju()
    def test_1(self):
        aaa = Cha_xun().cha(int(self.ss[1][0]))
        # print(aaa)
        self.assertEqual(aaa['errMsg'],'处理成功')

    def test_2(self):
        aaa = Cha_xun().cha(int(self.ss[2][0]))
        # print(aaa)
        self.assertNotIn( '处理成功',aaa)
if __name__ == '__main__':
    unittest.main()





