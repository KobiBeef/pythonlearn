# fhand = open('mbox-short.txt')
# for line in fhand:
# 	line = line.rstrip()
# 	if line.find('@uct.ac.za') == -1:
# 		continue
# 	print (line)

def exercise2():
	fname = input('filename: ')
	try:
		if fname != 'na na boo boo':
			fhand = open(fname)
		# elif fname == 'na na boo boo':
		elif fname == 'na na boo boo':
			print ("NA NA BOO BOO - you've been punk'ed")
			exit()
	except:
		print ('File:', fname ,'does not exist if cannot be openned')
		exit()

	count = 0
	datas = []
	for line in fhand:
		if line.startswith('X-DSPAM-Confidence: '):
			line = line.rstrip()
			count = count  + 1
			start = line.find(' ')
			extract_data = line[start:]
			data = float(extract_data)
			datas.append(data)
	print ('line count:', count, sum(datas)/len(datas))

exercise2()

def exercise1():
	fhand = input('Filename: ')
	try:
		fname = open(fhand)
	except:
		print ('file not found')

	print (fname.read())

# exercise1()