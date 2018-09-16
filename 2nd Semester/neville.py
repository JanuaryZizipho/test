##
# @brief	Algorithm for Neville's method.
# @author	Z. S. January (19255152@sun.ac.ca).
# @date		18 September 2018.

from numpy import zeros

def neville(x_data, y_data, x):
	"""p = neville(x_data, y_data, x)
	   Evaluate the polynomials interpolant p(x) that passes through the specified
	   data points by Neville's method."""


	n = len(x_data)
	p = zeros(n);

	for k in range(n):
		for i in range(n - k):
			if k == 0:
				p[i] = y_data[i]
			else:
				p[i] = (x - x_data[i+k] * p[i] + \
				(x_data[i] - x) * p[i+1]) / \
				(x_data[i] - x_data[i+k])

	return p[0];
