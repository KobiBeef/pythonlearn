######################
# note use python 3.4#
######################

def collatz00(number):
	data = int(number)
	if data%2 == 0:
		data = data / 2
		print (data)
		if data != 1:
			collatz(data)
	elif data%2 == 1:
		data = 3 * data + 1
		print (data)
		if data != 1:
			collatz(data)

# collatz(input("enter a number:"))

def collatz(data):
	try:
		data = int(data)
		if data == data:
			if data%2 == 0:
				data = data / 2
				print (data)
				if data != 1:
					collatz(data)
			elif data%2 == 1:
				data = 3 * data + 1
				print (data)
				if data != 1:
					collatz(data)
	except :
		print ("not integer")

# collatz(input("data input: "))