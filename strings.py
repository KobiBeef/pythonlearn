def exercise1():
	word = 'banana'
	index = 0
	for letter in word:
		index = index -1
		print (word[index])

# exercise1()

def exercise2():
	word = 'fruit'
	print (word[:])

# exercise2()

def exercise3():
	word = 'banana'
	count = 0
	for letter in word:
		if letter == 'a':
			count = count + 1
	print (count)

# exercise3()

def exercise4():
	word = 'banana'
	print (word.count('a'))

# exercise4()

def exercise5():
	string = 'X-DSPAM-Confidence: 0.8475'
	start = string.find(' ')
	print (start)

	end = string.find('5', start)
	print (end)

	extracted = string[start+1:]
	data = float(extracted)
	print (type(data), data)

exercise5()