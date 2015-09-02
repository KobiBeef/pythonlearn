import socket
import time
import urllib
import re
from BeautifulSoup import *

# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('www.py4inf.com', 80))
# mysock.send('GET http://www.py4inf.com/cover.jpg HTTP/1.0\n\n')

# count = 0
# picture = "";
# while True:
# 	data = mysock.recv(5120)
# 	if (len(data) < 1): break
# 	# time.sleep(0.25)
# 	count = count + len(data)
# 	print (len(data), count)
# 	picture = picture + data

# mysock.close()

# # Look for end of header
# pos = picture.find("\r\n\r\n");
# print ('Header length', pos)
# print (picture[:pos])

# # skip past the header and save the picture data
# picture = picture[pos+4:]
# fhand = open("stuff.jpg", "wb")
# fhand.write(picture);
# fhand.close()

# counts = dict()
# fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
# for line in fhand:
# 	words = line.split()
# 	for word in words:
# 		counts[word] = counts.get(word,0) + 1
# print counts

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve all of the achor tags
tags = soup('a')
for tag in tags:
	print 'TAG:', tag
	print 'URL:', tag.get('href', None)
	print 'Content:', tag.contents[0]
	print 'Attrs:', tag.attrs