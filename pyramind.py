# for i in range(1,7):
# 	for j in range(1,i):
# 		print (j, end='')
# 	print ()


# def pyramind(rows):
# 	for i in range(rows):
# 		print ('*'*(1*i+1) + ' '*(rows-i-1))

# pyramind(8)

def right_triangle(rows):	
	for i in range(rows):
		print ('*'*(1*i+1))

def upside_down_rigth_triangle(rows):
	for i in range(rows):
		print ('*'*(rows-i))

def reverse_rigth_triangle(rows):
	for i in range(rows):
		print (' '*(rows-i-1) + '*'*(1*i+1))

def upside_down_reverse_rith_triangle(rows):
	for i in range(rows):
		print (' '*(1*i) + '*'*(rows-i))

def full_triangle(rows):
	for i in range(rows):
		print (' '*(rows-i-1) + '*'*(2*i+1))

def line_vertical(rows):
	for i in range(rows):
		print ('*')

def line_horizontal(rows):
	print ('*')*rows

def reverse_full_triangle(rows):
	for i in range(rows):
		print (' '*(1*i) + '*'*(rows*2-i*2-1))		
		# print (' '*(1*i) + '*'*(rows*2-1-i*2))

def chessboard(rows):
	for y in range(rows): 
		print ('# ')*rows
		print (' #')*rows

# right_triangle(5)
# upside_down_rigth_triangle(5)
# reverse_rigth_triangle(5)
# upside_down_reverse_rith_triangle(5)
# full_triangle(5)
# reverse_full_triangle(5)
# line_vertical(5)
# line_horizontal(5)
# chessboard(5)
