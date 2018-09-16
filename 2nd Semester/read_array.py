import numpy as np
import re

def read_array(filename, dtype, separator='\\s+'):
	data = [[] for dummy in xrange(len(dtype))]
	with open(filename, 'r') as f:
		for line in f:
			#fields = line.strip().split(',')   # remove white space and split
			fields = re.split(separator, line.strip())
			print fields
			for i, number in enumerate(fields):
				data[i].append(number)
		
	for i in xrange(len(dtype)):	
		data[i] = np.cast[dtype[i]](data[i]) # converts the list of strings to a
											 # np array of ints

	return tuple(data)

if __name__ == '__main__':
	data = read_array('points.txt', (int, int))
	print data

