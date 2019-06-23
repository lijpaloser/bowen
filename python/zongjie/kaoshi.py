#!/use/bin/python
# _*_ coding:utf-8 _*_




#九九乘法表
def chengfa(x):
    for i in range(1,x):
        for j in range(1,i+1):
            sum = '{}*{}={}'
            print(sum.format(i,j,i*j),end='\t')
            if i == j :
                print('')
# chengfa(10)

#字符串不用int变成整数
# a = '123'
# b = a[::-1]
# c = 0
# for i in range(len(b)):
#     for j in range(1,10):
#         if str(j) == b [i]:
#             c +=j*(10**i)
# print(type(c))


#创建目录，在目录中创建a.txt文件，
# import os
# os.mkdir('aaa')
# with open('a.txt','w',encoding='utf-8') as f:
#     f.write('写入的数据')
# os.remove('a.txt')
# os.remove('aaa')


#将a.txt文件中的数据添加到数据库中
# import pymysql
# import  xlrd
# conn = pymysql.connect(host = '192.168.0.111',
#                        port = 3306,
#                        user = 'root',
#                        passwd = '123456',
#                        charset='utf-8')
#
# m = conn.cursor()
# m.execute('use test;')
# a = open(r'C:\\Users\\123\\PycharmProjects\\untitled4\\aa.txt','r')
# b = a.readlines()
# for i in range(4):
#     c = b[i]
#     s = c.split(',')
#     if i == 0:
#         continue
#         m.execute('create table gg ({} char(20),{} int,{} char(20 ));'.format(s[0], s[1], s[2]))
#     else:
#         m.execute('insert into gg values("{}","{}","{}")'.format(s[0], s[1], s[2]))
#     m.execute('select * from  gg;')
#     ff = m.fetchall()
# print(ff)



#发邮件

# import smtplib
# import  email.mime.multipart as mul
# import email.mime.text as text
# message = mul.MIMEMultipart()
# message['Subject'] = 'python_test'
# dd = ('lijp_1998@163.com')
# TB = ('1403380397@qq.com','825069672@qq.com')
# message['From'] = dd
# message ['To'] =','.join(TB)
# txt = '''
# 等候
# 老王离房东家很近哦
# '''
# tet = text.MIMEText(txt)
# message.attach(tet)
# smtp123 = smtplib.SMTP_SSL('smtp.163.com',465)
# smtp123.login('lijp_1998@163.com','li123456')
# smtp123.sendmail(dd,TB,message.as_string())
# smtp123.close()


#客户端
# import  socket
# sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# sock.connect(('192.168.0.83',3000))
# while True:
#     qq = input('>>>')
#     sock.send(qq.encode('utf-8'))
#     ww = sock.recv(1024)
#     print(ww.decode('utf-8'))


#爬虫
import requests
import  re
import json
import xlwt
import xlrd
url = 'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=653&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&=0&_v=0.80308920&x-zp-page-request-id=5c8f4da4d99d4804a7cfcc6af51cd95b-1557229106436-265543'
head = {
         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'
        }
res = requests.get(url,headers = head)
html = res.content.decode('utf-8')
qqq = json.loads(html)
b = []
for j in range(0,90):
    a = qqq['data']['results'][j]['company']['name'],qqq['data']['results'][j]['jobName'],qqq['data']['results'][j]['salary'],qqq['data']['results'][j]['eduLevel']['name']
    b.append(a)
print(b)
ff = xlwt.Workbook(encoding='utf-8')
sheet = ff.add_sheet('zhilian')
c = ['公司名称','公司职位','薪资','文凭']
for i in range(len(c)):
    sheet.write(0,i,c[i])
for k in range(len(b)):
    for t in range(len(b[k])):
        sheet.write(k+1,t,b[k][t])
ff.save('pachong.xls')
# import  pymysql
# import  xlrd
# conn = pymysql.connect(host='192.168.0.200',
#                        port=3306,
#                        user='root',
#                        passwd='123456')
# f = xlrd.open_workbook('pachong.xls')
# m=conn.cursor()
# m.execute('use test')
# sheet = f.sheets()[0]
# # a = sheet.nrows
# for i in range(sheet.nrows):
#     b = sheet.row_values(i)
#     if i == 0:
#         #continue
#         m.execute('create table ljp({} char(250),{} char(250),{} char(250),{} char(250));'.format(b[0],b[1],b[2],b[3]))
#     else:
#         m.execute('insert into ljp values("{}","{}","{}","{}");'.format(b[0],b[1],b[2],b[3]))
#         m.execute('select * from ljp;')
# print(m.fetchall())




#服务器


