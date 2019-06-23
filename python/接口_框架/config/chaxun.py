# !/usr/bin/puthon
# # _*_coding:utf_8  _*_

#查询订单列表
import  requests
import sys
sys.path.append(r'C:\Users\123\PycharmProjects\untitled4\接口_框架')
from 接口_框架.data.duqu_dingdan import shuju



class Cha_xun(object):
    def cha(self,num):
        url = "https://mobileqa.dms.saic-gm.com/api/dev/pol4s/pol4sPartOrder/rest/pol4s/partOrder/orderList"
        header = {
             'Content-Type': "application/json",
            'x-dealer-code': "2100001",
            'x-position-code': "D_PO_1028",
            'x-resource-code': "pol4s_partOrder_orderList",
            'x-track-code': "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
            'x-user-code': "dhxc1u",
            'x-access-token': "c909d3541a63a46b75f314a4e94828c0",
            'User-Agent': "PostmanRuntime/7.15.0",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Postman-Token': "96b84fe6-f881-4caf-935f-51a14acf64a9,643bc70f-24ae-4c97-8d42-3f440c51d319",
            'Host': "mobileqa.dms.saic-gm.com",
            'cookie': "dapp.sgm.com:qa:=4bc41a7b89de10da2cb72d7cc19dbb9b; dapp.sgm.com:qa:=4bc41a7b89de10da2cb72d7cc19dbb9b; fdaa0f2d854071f7f82d1c80a99830bb=2d45a497bf053a6a9a23955ddef3f0bd; a689baa2b7060531c4d0be5b10aa7055=b1100f0adf89b706031ddd7ab44c593f",
            'accept-encoding': "gzip, deflate",
            'content-length': "193",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
        }
        #变量名，放置参数
        pyloa =   "{\r\n \"pageNum\": %s,\r\n \"pageSize\": 10,\r\n \"queryTerms\": {\r\n  \"orderType\": \"\",\r\n  \"orderStatus\": \"\",\r\n  \"orderDelayFlag\":\"\",\r\n  \"orderNo\": \"\",\r\n  \"startReportDate\": \"\",\r\n  \"endReportDate\": \"\"\r\n }\r\n}" % (num)
        res = requests.post(url=url,headers=header,data=pyloa)
        return res.json()

if __name__ == '__main__':
   print(Cha_xun().cha(1))
   #  for i in shuju():
   #      print(i)
   #      a = Ding_dan().cha(i)
   #      print(a)

