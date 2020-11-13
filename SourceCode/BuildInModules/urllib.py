# _*_ coding: utf-8 _*_
'''
urlLib  give a series Operator about URL
'''
# resques module is powerful tool to get http request

from urllib import request

with request.urlopen("https://api.douban.comv2/book/2129650") as f:
    data = f.read()
# now we get http page's data store in data variable
# And print statu
    print("status", f.status, f.reason)

# By Proxy bypass  we need ProxyHandler to deal with
proxy_handler = request.proxy_handler({"http" : "http://127.0.0.1:51837"})

# using user-agent for simulating webnet browers 