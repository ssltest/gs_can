#!/usr/bin/env python
#Gscan
#date : 20141210

import sys
def filter(lines):
	ipPorts = {}
	for line in lines:
		line = line.strip()
		if len(line.split('|')) > 1:
			status = line.split('|')[0]
			ipPort = line.split('/')[0]
			if status == '200' or status == '302':
				if ipPort in ipPorts.keys():
					ipPorts[ipPort] = ipPorts[ipPort] + 1
				else:
					ipPorts[ipPort] = 0
			elif status == '404' or status == '403':
				ipPorts[ipPort] = 0
	return ipPorts


if "__main__":
	inFile = sys.argv[1]
	if len(sys.argv) > 2:
		getStat = sys.argv[2]
	else:
		getStat = 0
	f = open(inFile,'r')
	lines = f.readlines()
	ipPorts = filter(lines)
	ipPortKeys = ipPorts.keys()
	for line in lines:
		line = line.strip()
		if len(line.split('|')) > 1:
			ipPort = line.split('/')[0]
			if ipPort in ipPortKeys:
				if ipPorts[ipPort] < 10 and getStat == 0:
					print line
				elif ipPorts[ipPort] < int(getStat) and line.split('|')[0] == '200':
					url = 'http://' + line.split('200|')[1]
					print url
				else:
					pass
