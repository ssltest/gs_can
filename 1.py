f = open('all.txt','r')
for i in f.readlines():
	i = i.strip()
	if i.find('/') == -1:
		print "/" + i
	else:
		print i
