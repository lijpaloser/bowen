#!/use/bin/python
# _*_ coding:utf-8 _*_6


import socket
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind(('192.168.0.83',3000))
# s.listen(3)
# while  True:
#     client,addr = s.accept()
#     print(client)
#     while True:
#         reg = client.recv(1024)
#         print(reg.decode('utf-8'))
#         msg = input('>>>')
#         client.send(msg.encode('utf-8'))


#爬

# class  FreeBuf:
#     def send_qingqiu(self,page,):
#         url = 'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=653&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&=0&_v=0.80308920&x-zp-page-request-id=5c8f4da4d99d4804a7cfcc6af51cd95b-1557229106436-265543'.format(page)
#         head = {
#             'User-Agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'
#         }
#         #发送请求
#         res = requests.get(url,headers = head)
#         #读取结果  1 text:以文本的方式接受，结果是一个字符串
#                 #  2 content，是以字节的方式接受，以字节的形式接受
#         #print(res.text)
#         hh = res.content.decode('utf-8')
#         return hh
#             # 二次过滤
#     def guolv(self,x):
#         title = []
#         patt = re.compile('<div class="news-info">(.*?)<dd>',re.S)#(过滤)
#         itesms = patt.findall(x)
#         for i in itesms:
#             aa = re.findall('title="(.*?)"',i)
#             title.append(aa[0])
#         return title
#             #保存
#     def baocun(self,y):
#         with open('ab.txt','a',encoding='utf-8')  as f :
#             for i in y :
#                 f .write(i+'\n')






# #数据库导入到excel
# import  pymysql
# import xlwt
# conn = pymysql.connect(host='192.168.0.12',
#                        port = 3306,
#                        user = 'root',
#                        passwd = 'tiger')
# m = conn.cursor()
# m.execute('use python')
# m.execute('desc gg')
# a = m.fetchall()
# c = []
# with open('a.tet','w',encoding='utf-8') as f:
#     for i in range(len(a)):
#         c.append(a[i][0])
#         f.write('{}'.format(c[i]))
# f.write('\n')
# m.execute('select * from gg:')
# b = m.fetchall()
# for i in range(len(b)):
#     p = b[i]
#     for k in range(len(p)):
#         f.write('{}'.format(p[k]))


# #爬虫
# import requests
# import  re
# class pachong:
#     def send_paqu(self):
#         url = {}
#         head = {
#
#         }
#         html = requests.get(url,headers=head)
#         hh = html.content.decode('utf-8')
#         return hh
#     def guo_paqu(self,x):
#         guo = re.compile('')
#         lu = guo.findall(x)
#         return lu
#     def save_paqu(self,y):
#         with open('a.txt','a',encoding='utf-8')  as f :
#             for i in y :
#                 f.write(i + '\n')



# import socket
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind('192.168.0.42')
# s.listen(3)
# while True:
#     client,add =s.accpt()
#     print(client)
#     reg = client.rev('1024')
#     print(reg.decode('utf-8'))
#     msg = input('>>>')
#     client.sent(msg.encode('utf-8'))


#客户端
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.connect('192.168.0.42')
# while True:
#     msg = input('>>>')
#     s.send(msg.encode('utf-8'))
#     w = s.rev('1024')
#     print(w.decode('utf-8'))
#
# import  reuests
# import re
# uil=''
# head=''
# rel=request.




