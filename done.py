# USE PTHON 3.4
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
	if len(nums) == 0:
		print ('division by zeron')	
	else:
		print (sum(nums), len(nums), sum(nums)/len(nums))

total_count_ave()