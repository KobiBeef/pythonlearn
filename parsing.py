import xml.etree.ElementTree as ET
import json
import urllib

testxml = open('testxml.xml').read()
tree = ET.fromstring(testxml)
# print 'Name:', tree.find('name').text()
# print 'Attr:',tree.find('email').get('hide')

testjson = open('test.json').read()
info = json.loads(testjson)

# for item in info:
# 	print 'Name', item['name']
# 	print 'Id', item['id']
# 	print 'Attribute', item['x']

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
	address = raw_input('Enter location: ')
	if len(address) < 1: break

	url = serviceurl + urllib.urlencode({'sensor': 'false', 'address': address})
	print 'Retrieving', url
	uh = urllib.urlopen(url)
	data = uh.read()
	print 'Retrieved', len(data), 'characters'

	try: js = json.loads(str(data))
	except: js = None
	if 'status' not in js or js['status'] != 'OK':
		print '==== Failure To Retrieve ===='
		print data
		continue

	print json.dumps(js, indent=4)
	lat = js["results"][0]["geometry"]["location"]["lat"]
	lng = js["results"][0]["geometry"]["location"]["lat"]
	print 'lat', lat, 'lng', lng
	location = js['results'][0]['formatted_address']
	print location