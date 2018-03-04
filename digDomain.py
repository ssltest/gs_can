#!/usr/bin/python

import requests
import threading
def digg(site,domain):
	result = {}
	try:
		headers = {"Host":domain}
		r = requests.get(site,headers=headers,verify=False)
		code = r.headers['Content-Length']
	except Exception,e:
		code = '-1'
	result['site'] = site
	result['domain'] = domain
	result['code'] = code
	print result['site']+"||"+result['domain']+"||"+result['code']
	return  result

if "__main__":
	site = 'https://23.42.179.82/'
	dom = '.zomato.com'
	#res = digg(site,domain)
	#print res['site']+"||"+res['domain']+"||"+res['code']
	f = open("domain.dict","r")
	fs = f.readlines()
        threads = []
        for d in fs:
                d = d.strip()
		domain = d + dom
                t = threading.Thread(target=digg,args=(site,domain))
                threads.append(t)

        num = 0
        for t in threads:
                t.start()
                while True:
                        if(len(threading.enumerate()) < 11):
                                break
