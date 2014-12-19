#!/usr/bin/env python
##################################
#
#name	:	getIpAndPort.py
#author	:	goderci
#date	:	2013.11.15	
#
##################################

import re
import sys
import urllib2
import httplib

def isIp(line):
	if re.search('report for',line):
		ip = re.match('.*([^0-9]{1})([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})([^0-9]{1}).*',line)
		return ip.groups()[1]
	else:
		pass

def getIpAndPort(nmapResult):
	ipAndPort = {}
	port = []
	ip = ''
	for line in nmapResult:
		if isIp(line):
			#ipAndPort[ip] = port
			ip = isIp(line)
			print ip
			port = []
		elif re.search('^([0-9]+\/tcp)([^a-z]+)open(.*)',line):
			#80/tcp   open  http?
			print ip
			portNum = re.match('^([0-9]+)\/tcp([^a-z]+)open(.*)',line).groups()[0]
			#if re.search('(.*)http(.*)',line) or 7999<int(portNum)<10000:
			if 1<int(portNum)<30000:
				port.append(portNum)
			else:
				pass
			ipAndPort[ip] = port
		else:
			pass
#	print ipAndPort
#	print len(ipAndPort.keys())
	result = ''
	for k in range(len(ipAndPort)):
		for j in range(len(ipAndPort.values()[k])):
			result = ipAndPort.keys()[k] + ':' + ipAndPort.values()[k][j]
			print result

def getHttpStatus(ipAndPort,dictLine):
        try:
                conn = httplib.HTTPConnection(ipAndPort,timeout=1)
                conn.request('GET',dictLine)
                result = conn.getresponse()
                resultStatus = result.status
                content=result.read()
                conn.close()
                return resultStatus
        except:
                return "time out"

def getHttpStatus2(urlInput):
        try:
                result = urllib2.urlopen(urlInput,timeout=1)
                return result.getcode()
        except urllib2.HTTPError, e:
                return e.code
        except:
                return "time out"

def weekScan(ipAndPort,scanDict):
	result = []
	for i in ipAndPort:
		i = i.strip()
		for j in scanDict:
			j = j.strip()
			status = str(getHttpStatus(i,j))
			if status == '200':
				url = 'http://' + i + j
				print '200---' + url
				#result.append(url)i
			else:
				url = 'http://' + i + j
				print status + '---' + url
	return result
			

if "__main__":
	#filename = '/home/goderci/python/tools/result/sina/sina.nmap'
	filename = sys.argv[1]
	f = open(filename,'r')
	fileLine = f.readlines()
	ipAndPort = getIpAndPort(fileLine)
	#print ipAndPort
