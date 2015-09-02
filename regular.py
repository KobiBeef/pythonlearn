import re
# hand = open('mbox-short.txt')
# for line in hand:
# 	line = line.rstrip()
# 	if re.search('^From:.+?@', line):
# 		print (line)

# s = 'Hello from csev@umich.edu to cwen@iupui.edu about the meeting @2PM'
# lst = re.findall('\S+@\S+', s)
# print (lst)


# for line in hand:
# 	line = line.rstrip()
# 	x = re.findall('^X\S*: ([0-9.]+)', line)
# 	if len(x) > 0:
# 		print (x)
# count = 0

def ex1():
	hand = open('mbox.txt')
	fline = input('search for: ')
	count = 0
	for line in hand:
		line = line.rstrip()
		x = re.findall(fline, line)
		if len(x) > 0:
			count = count + 1

	print (hand.name, 'has',count , 'lines that matched')

def ex2():
	fname = input('Enter file: ')
	fhand = open(fname)
	flist = list()
	count = 0
	for line in fhand:
		line = line.rstrip()
		x = re.findall('^New Revision:.([0-9.]+)', line)
		for i in x:
			count = count + 1
			num = int(i)
			flist.append(num)
	print (sum(flist)/count)