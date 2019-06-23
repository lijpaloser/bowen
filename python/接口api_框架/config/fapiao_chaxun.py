# !/usr/bin/puthon
# # _*_coding:utf_8  _*_

#发票查询
import  requests
import sys
sys.path.append(r'C:\Users\123\PycharmProjects\untitled4\接口api_框架')
from 接口api_框架.data.duqu_dingdan import shuju



class Cha_xun(object):
    def cha(self):
        url =  "https://mobileqa.dms.saic-gm.com/api/sit/pol4s/pol4sPartOrder/rest/pol4s/partOrder/orderElectricInvoice"
        header = {
            'Content-Type': "application/json",
            'x-dealer-code': "2100001",
            'x-position-code': "D_PO_1028",
            'x-resource-code': "pol4s_partOrder_orderElectricInvoice",
            'x-track-code': "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
            'x-user-code': "dhxc1u",
            'x-access-token': "8405e48dd499a8a329afe8e8d8e7da3b",
            'User-Agent': "PostmanRuntime/7.15.0",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Postman-Token': "ac4c804d-3f62-4583-b391-c16715b73001,010ec98e-2d3a-43ab-9fc2-af246588ce4b",
            'Host': "mobileqa.dms.saic-gm.com",
            'cookie': "dapp.sgm.com:qa:=8405e48dd499a8a329afe8e8d8e7da3b; dapp.sgm.com:qa:=8405e48dd499a8a329afe8e8d8e7da3b; fdaa0f2d854071f7f82d1c80a99830bb=2d45a497bf053a6a9a23955ddef3f0bd; a689baa2b7060531c4d0be5b10aa7055=b1100f0adf89b706031ddd7ab44c593f",
            'accept-encoding': "gzip, deflate",
            'content-length': "37",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
        }
        #变量名，放置参数
        pyloa =  "{\r\n \"orderNo\": \"R2100005181116190\"\r\n}"
        res = requests.post(url=url,headers=header,data=pyloa)
        return res.json()

if __name__ == '__main__':
   print(Cha_xun().cha())
   #  for i in shuju():
   #      print(i)
   #      a = Ding_dan().cha(i)
   #      print(a)

