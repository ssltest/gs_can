#!/usr/bin/env python
#use python-nmap to scanner ip
import nmap
import sys
import threading


def scan(ip,port):
        nm = nmap.PortScanner()
	#argus = '-p ' + port + ' -T4'
	argus = '-T4'
        result = nm.scan(hosts=ip, arguments=argus)
        for host in nm.all_hosts():
                for proto in nm[host].all_protocols():
                        lport = nm[host][proto].keys()
                        lport.sort()
                        for port in lport:
                                if nm[host][proto][port]['state'] == 'open':
                                        ipPort = host + ':' + str(port)
                                        print ipPort

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
