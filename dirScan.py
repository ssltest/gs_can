#!/usr/bin/env python
##################################
#
#name   :       dirScan.py
#author :       goderci
#date   :       2014.02.25      
#
##################################

import re
import sys
import urllib2
import httplib
import getopt
import time
import os
import threading

tOutip = []
ip200 = {}

def getHttpStatus(ipAndPort,dictLine):
        try:
		isHttp = ipAndPort.find('http://')
		if isHttp == 0:
			ipAndPort = ipAndPort.split('http://')[1]
			if ipAndPort.find('/') > 0:
				ipAndPort = ipAndPort.split('/')[0]
                conn = httplib.HTTPConnection(ipAndPort,timeout=2)
                conn.request('GET',dictLine)
                result = conn.getresponse()
                resultStatus = result.status
                content=result.read()
                conn.close()
                return resultStatus
        except:
                return "time out"


def weekScan(i,scanDict):
	global tOutip
	global ip200
        result = []
	i = i.strip()
	for j in scanDict:
		ip200key = ip200.keys()
		if i in tOutip:
                	return 0
	        elif i in ip200key:
                	if ip200[i] > 50:
                        	return 1		
	        j = j.strip()
	        status = str(getHttpStatus(i,j))
		if status == 'time out':
			tOutip.append(i)
		elif status == '200':
			if i in ip200.keys():
				ip200[i] = ip200[i] + 1
			else:
				ip200[i] = 1
	        url = status + '|' + i + j
	        #result.append(url)
		print url

if "__main__":
        print "##################################"
        print "#                                #"
        print "#        dirScan 1.0 by goderci  #"
        print "#                                #"
        print "##################################"
        print "if you need help,please input -h/--help,:)"

        scanUrl = ''
        scanFile = ''
        scanDict = ''
	scanDir = ''
	scanList = []	

        try:
                options,args = getopt.getopt(sys.argv[1:],"hf:u:d:l:",["help","url=","file=","dict=","list"])
        except getopt.GetoptError:
                print "input is error,if you need help,please input -h/--help"
        for name,value in options:
                if name in ("-h","--help"):
                        print "-f\t: input urllist by a file,like -f url.txt"
                        print "--file=\t: input iplist by a file,like --file=url.txt"
                        print "-u\t: input ip to scan,like -u http://www.baidu.com"
                        print "--url=\t: input ip to scan,like --url=url.txt"
                        print "-d\t: input a dict to scan,like -d dict.txt"
                        print "--dcit=\t: input a dict to scan,like --dict=dict.txt"
			print "-l=\t: input a dir to scan,like -l dir.txt"
                if name in ("-u","--url"):
                        scanUrl = value
                if name in ("-f","--file"):
                        scanFile = value
                if name in ("-d","--dict"):
                        scanDict = value
		if name in ("-l","--list"):
			scanDir = value
        if len(scanDict) == 0:
                print "you need input dict!"
                sys.exit()
        elif len(scanUrl) == 0 and len(scanFile) == 0:
                print "you need input url or urllist"
                sys.exit()
        elif len(scanUrl) != 0 and len(scanFile) != 0:
                print "you need input url or urllist"
                sys.exit()
        elif len(scanUrl) != 0 and len(scanFile) == 0:
		scanList.append(scanUrl)
        elif len(scanUrl) == 0 and len(scanFile) != 0:
		scanFileOpen = open(scanFile,'r')
		scanList = scanFileOpen.readlines()
        else:
                print "please check input!"
                sys.exit()
	print "\n-------start at : " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "-------"
	
	fDict = open(scanDict,'r')
	if len(scanDir) == 0:
		dictLine = fDict.readlines()
	else:
		dictLine = []
		dDir = open(scanDir,'r')
		for dirLine in dDir.readlines():
			for dLine in fDict.readlines():
				dictLineO = dirLine.strip() + dLine.strip()
				dictLineY = dictLineO.replace('//','/')
				dictLine.append(dictLineY)
	#weekScan(scanList,dictLine)
	threads = []
	for i in scanList:
    		t = threading.Thread(target=weekScan,args=(i,dictLine))
		threads.append(t)

	num = 0
	for t in threads:
		t.start()
		while True:
	    		if(len(threading.enumerate()) < 31):
	        		break
