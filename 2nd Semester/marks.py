import hashlib

def marks():

	s = ''
	name = hashlib.sha1(s.encode('utf-8')).hexdigest()[:5]
	print (name)

marks()
