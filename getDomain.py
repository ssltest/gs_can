#!/usr/bin/env python
#python getDomain.py rizhiyi.com domain.dict
import sys
import time
import socket


def host2ip(host):
	try:
		results=socket.getaddrinfo(host,None)
		for result in results:
			if str(result[4][0]).find('.') > -1:
				print host, result[4][0]
	except Exception,e:
		pass

host = sys.argv[1]
dictFile = sys.argv[2]

f = open(dictFile,'r')
for i in f:
	domain = i.strip() + '.' + host
	host2ip(domain) 
