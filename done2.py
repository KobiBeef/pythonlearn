# USE PYTHON 3.4
def total_count_ave():
	nums = []
	while True:
		numbers = input('Enter number: ')
		try:
			if numbers != 'done':
				number = int(numbers)
				nums.append(number)
				# print (nums)
			elif numbers == 'done':
				break
		except:
			print ('Enter proper data type')
	print ('summation of numbers:', sum(nums), 'number of entries:', len(nums), 'largest number:', max(nums), 'smallest number:', min(nums))

total_count_ave()

# fruit = 'fruit'
# index = -1
# while index < len(fruit):
# 	letter = fruit[index]
# 	print (letter)
# 	index = index - 1