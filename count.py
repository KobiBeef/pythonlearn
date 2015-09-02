def count():
	word = input('enter word: ')
	letters = dict()
	for letter in word:
		letters[letter] = letters.get(letter, 0) + 1
	print (letters)

# count()

# word = 'banana'
# count = 0
# for letter in word:
# 	if letter == 'a':
# 		count = count + 1

# print (count)

string = input('enter string: ')
letter = input('enter letter within string: ')

def count2(string, letter):
	count = 0
	if letter in string:
		print ('letter in string')
		for x in string:
			if x == letter:
				count = count + 1
		print ('there are', count, letter)
	else:
		print ('letter not in string')

count2(string, letter)