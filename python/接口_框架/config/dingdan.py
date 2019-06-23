# !/usr/bin/puthon
# # _*_coding:utf_8  _*_

#订单明细

import requests


class Ding_dan(object):
    def D_ing(self):
        url = "https://mobileqa.dms.saic-gm.com/api/sit/pol4s/pol4sPartOrder/rest/pol4s/partOrderSearch/partOrderDetailSearch"
        header = {
            'Content-Type': "application/json",
            'x-dealer-code': "2100005",
            'x-position-code': "D_PO_1028",
            'x-resource-code': "pol4s_partOrderSearch_partOrderDetailSearch",
            'x-track-code': "4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394",
            'x-user-code': "dhxc1u",
            'x-access-token': "df634bc12d87fb0d152a9852a0fa3f45",#c909d3541a63a46b75f314a4e94828c0
            'User-Agent': "PostmanRuntime/7.15.0",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Postman-Token': "b881672d-9fbb-4ec9-aa85-3738cfb184a1,a3b2ac76-68a3-4d07-b4d8-6b1adede99d6",
            'Host': "mobileqa.dms.saic-gm.com",
            'cookie': "dapp.sgm.com:qa:=cb9857a88de51876e5166a61b86993dd; dapp.sgm.com:qa:=cb9857a88de51876e5166a61b86993dd; fdaa0f2d854071f7f82d1c80a99830bb=2d45a497bf053a6a9a23955ddef3f0bd; a689baa2b7060531c4d0be5b10aa7055=b1100f0adf89b706031ddd7ab44c593f",
            'accept-encoding': "gzip, deflate",
            'content-length': "96",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
        }
        pyloa = "{\r\n \"pageNum\":\"1\",\r\n \"pgeSize\":\"10\",\r\n \"queryTerms\":\r\n {\r\n  \"orderNo\":\"V2100880181219390\"\r\n }\r\n}"
        res = requests.post(url=url,headers=header,data=pyloa)
        return res.json()
if __name__ == '__mian__':
   print(Ding_dan().D_ing())
