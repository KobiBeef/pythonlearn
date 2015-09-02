test_list = [1 , 2 ,3, 4, 5]

def exercise1a(test_list):
	new_list = list()
	test_list = test_list
	new_list.append(test_list[0])
	new_list.append(test_list[-1])
	print (new_list)

def exercise1b(test_list):
	test_list = test_list
	new_list = test_list[1:-1]
	return new_list

def exercise2():
	fhand = open('mbox-short.txt')
	count = 0
	for line in fhand:
		words = line.split()
		if len(words) == 0 or words[0] != 'From': continue
		print (words[2])

def exercise4():
	fname = input('filename: ')
	fhand = open(fname)
	flist = list()
	for line in fhand:
		words = line.split()
		for word in words:
			flist.append(word)

	flist.sort()
	print (flist)

def exercise5():
	fname = input('Filename: ')
	fhand = open(fname)
	count = 0
	flist = list()
	for line in fhand:
		words = line.split()
		word = 'From'
		if word in words:
			flist.append(words[1])
			print (words[1])

# exercise5()