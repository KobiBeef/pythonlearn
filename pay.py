
def compute_pay():
	while True:
		hours = input("Enter hours: ")
		rate = input("Enter rate: ")
		try:
			if len(hours) == 0 or len(rate) == 0:
				print ('enter a value')
			else:
				num_hours = float(hours)
				num_rate = float(rate)
				if num_hours > 40:
					overtime_hours = num_hours - 40
					overtime_pay = overtime_hours * (num_rate * 1.5)
					regular_pay = (num_hours - overtime_hours) * num_rate
					pay = overtime_pay + regular_pay
					print (pay)
					break
				else:
					regular_pay = num_hours * num_rate
					print (regular_pay)
					break
		except:
			print('Enter numeric numbers only')

compute_pay()