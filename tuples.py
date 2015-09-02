def exercise1():
	fname = input('Filename: ')
	fhand = open(fname)
	fdict = dict()
	flist = list()

	try:
		for line in fhand:
			words = line.split()
			if 'From' in words:
				fdict[words[1]] = fdict.get(words[1], 0) + 1
		
		for key, value in fdict.items():
			flist.append((value, key))
		flist.sort()

		h_value, h_key = flist[-1]
		print(h_key, h_value)

	except:
		print ('filename not found')

# exercise1()

def exercise2():
	fname = input('Filename: ')
	fhand = open(fname)
	fdict = dict()
	flist = list()
	hour = list()

	try:
		for lines in fhand:
			words = lines.split()
			if 'From' in words:
				flist.append(words[5])

		for time in flist:
			start = time.find(':')
			hours = time[start-2:start]
			fdict[hours] = fdict.get(hours, 0) + 1

		for key, value in fdict.items():
			hour.append((int(key), value))

		hour.sort()
		for hour, count in hour:
			print (hour, count)
	except:
		print ('file not found')
exercise2()		