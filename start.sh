#!/bin/bash
#date	:	2014.02.28

baiduIpduan=$1
activeDir=./activeIp/
nmapResult=./nmapResult/
ipPortDir=./ipPort/
dirScanDir=./dirScan/
scanDate=$(date +%Y%m%d)

#kill this scan last day
for i in `ps aux|grep 'nmap -iL activeIp'|grep 'host'|awk '{print $2}'`;do kill -9 $i;done

#get active ip
fileName=$activeDir$scanDate
#fileName=./activeIp/20140505
resultFile=$nmapResult$scanDate.nmap
ipPortFile=$ipPortDir$scanDate
dirScanFile=$dirScanDir$scanDate

#nmap -iL $baiduIpduan -sP -T4 --host_timeout 30s|grep -o -E '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'|sort|uniq > $fileName

#nmap -iL $fileName -p 8005,8064,8065,8095,8110,8029,8122,8200,8083,8208,8099,8100,8888,8092,8070,8071,8085,8030,8082,8111,8091,8104,8081,8103,8088,8090,8101,8102,8000,8016,8015,8014,8013,8017,8018,8006,8012,8011,8007,8003,8010,8002,8004,8008,8020,8019,8001,8009,8080,80 -T4 > $resultFile
#python getIpPort.py $resultFile > $ipPortFile
nohup python pyNmapIpPort.py $baiduIpduan > $ipPortFile 2>&1 
nohup python dirScan.py -f $ipPortFile -d dict.txt > $dirScanFile 2>&1 
