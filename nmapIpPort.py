#!/usr/bin/env python
#use nmap to scanner ip
import sys
import threading
import os
import re

def isIp(line):
        if re.search('^Interesting ports on',line):
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
                        port = []
                elif re.search('^([0-9]+\/tcp)([^a-z]+)open(.*)',line):
                        #80/tcp   open  http?
                        portNum = re.match('^([0-9]+)\/tcp([^a-z]+)open(.*)',line).groups()[0]
                        #if re.search('(.*)http(.*)',line) or 7999<int(portNum)<10000:
                        if 1<int(portNum)<30000:
                                port.append(portNum)
                        else:
                                pass
                        ipAndPort[ip] = port
                else:
                        pass
#       print ipAndPort
#       print len(ipAndPort.keys())
        result = ''
        for k in range(len(ipAndPort)):
                for j in range(len(ipAndPort.values()[k])):
                        result = ipAndPort.keys()[k] + ':' + ipAndPort.values()[k][j]
                        print result

def scan(ip,port):
	argus = 'nmap ' + ip + ' -p ' + port + ' -T4'
	res = os.popen(argus).readlines()
	result = getIpAndPort(res)
	if result is not None:
		print result

	

if "__main__":
	ipduanFile = sys.argv[1]
        ipF = open(ipduanFile,'r')
       	ips = ipF.readlines()
	#ports = '22,80-90,8000-9000,3306,5800-5810,5900-5910,10000,20000,30000,40000,50000,2222'
	ports = '22,3306,3389,8000-9000,80-90'
        threads = []
        for ip in ips:
		ip = ip.strip()
                t = threading.Thread(target=scan,args=(ip,ports))
                threads.append(t)

        num = 0
        for t in threads:
                t.start()
                while True:
                        if(len(threading.enumerate()) < 11):
                                break
