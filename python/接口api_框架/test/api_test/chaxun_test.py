# !/usr/bin/puthon
# # _*_coding:utf_8  _*_
from 接口api_框架.config.fapiao_chaxun import Cha_xun
from  接口api_框架.config.baogao import B_gao
# from  接口_框架.data.duqu_dingdan import shuju
import unittest
class C_xun(unittest.TestCase):
    # ss = shuju()
    def test_1(self):
        aaa = Cha_xun().cha()
        print(aaa)
        self.assertEqual(aaa['errMsg'],'处理成功')

    def test_2(self):
        aaa = Cha_xun().cha()
        print(aaa)
        self.assertNotIn( '处理成功',aaa)
if __name__ == '__main__':
    # unittest.main()
    B_gao((C_xun("test_1"),C_xun("test_2")),report_path=r'C:\Users\123\PycharmProjects\untitled4\接口api_框架\report\aaa.html')



