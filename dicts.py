# import string

# fname = input('Enter file: ')
# try:
# 	fhand = open(fname)
# except :
# 	print ('File cannot be opened:', fname)
# 	exit()

# counts = dict()
# for line in fhand:
# 	line = line.translate(line.maketrans("",""), string.punctuation)
# 	line = line.lower()
# 	words = line.split()
# 	for word in words:
# 		if word not in counts:
# 			counts[word] = 1
# 		else:
# 			counts[word] += 1
# print (counts)

def exercise2():
	fname = input('Filename: ')
	fhand = open(fname)
	fdict = dict()
	# day = list()
	# date = list()
	for line in fhand:
		words = line.split()
		word = 'From'
		if word in words:
			fdict[words[2]] = fdict.get(words[2],0) + 1
	print (fdict)

# exercise2()
def exercise3():
	fname = input('Filename: ')
	fhand = open(fname)
	fdict = dict()
	for line in fhand:
		words = line.split()
		if 'From' in words:
			fdict[words[1]] = fdict.get(words[1],0) + 1
	print (fdict)

exercise3()

def exercise4():
	fname = input('Filename: ')
	fhand = open(fname)
	fdict = dict()
	for line in fhand:
		words = line.split()
		if 'From' in words:
			fdict[words[1]] = fdict.get(words[1], 0) + 1
	test = fdict.values()
	test.sort()
	for value in test:
		print (value, fdict[value])

# exercise4()

def exercise5():
	fname = input('Filename: ')
	fhand = open(fname)
	fdict = dict()
	flist = list()
	for line in fhand:
		words = line.split()
		if 'From' in words:
			flist.append(words[1])
	for mail in flist:
		start = mail.find('@')
		domain = mail[start+1:]
		fdict[domain] = fdict.get(domain, 0) + 1
	print (fdict)

# exercise5()