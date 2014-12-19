#!/usr/bin/env python
#python pro.py proNum cmdfile infile outfile
#python pro.py 4 text.py infile outfile
import os
import time
import sys
if "__main__":
	num = int(sys.argv[1]) - 1
	cmdfile = sys.argv[2]
	infile = sys.argv[3]
	outfile = sys.argv[4]
	y = sys.argv[5]
	tnow = time.strftime('%s',time.localtime(time.time()))
	f = open(infile,'r').readlines()
	lenFile = len(f)
	oneNo = lenFile/num
	for n in range(num + 1):
		n1 = n + 1
		tmpFile = tnow + '.pro.tmp.' + str(n)
		output = open(tmpFile, 'w+')
		x = oneNo * n
		y = oneNo * n1
		if n == num and y > lenFile:
			x = num * oneNo
			y = lenFile
		else:
			pass
		for l in range(x,y):
			output.write(f[l])
		cmd = 'python ' + cmdfile + ' ' + tmpFile + ' >> ' + outfile + ' 2>&1'
		if y == 'yes':
			os.popen(cmd)
		else:
			print cmd
		
