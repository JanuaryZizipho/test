##
# @brief 	Romberg integration algorithm.
# @author	Z. S. January (19255152@sun.ac.za)
# @date		18 September 2018

import numpy as np
#from trapezoid import trapezoid

def romberg(f, a, b, tol=1.0e-6):
	"""
	I, n_panels = romberg(f, a, b, tol=1.0e-6)	

	Return the integral from a to b of f(x), by Romberg Integration,
	as well as the number of panels used.
	"""
	# panels to trapezoid --> k = 2 ** i-1
	# h = b - a / k 

	n = 4
	R = np.zeros((n, n))
	n_panels = 0
	h = b - a
	i_val = 0
	j_val = 0

	for i in range(0, n):
		k = 2 ** i 
		n_panels = k
		h = h / 2
		R[i, 0] = trapezoid(f, a, b, k)

		for s in range(0, i):
			j = s + 2
			R[i, s+1] = 1.0 / (4 ** (j-1) -1)*(4 ** (j-1) * R[i, s] - R[i-1, s])

		if (i > 1): 
			if abs(R[i, s+1] - R[i, s]) < tol:
				break

	print R[0,0], R[0,1], R[0, 2], R[0, 3]
	print R[1,0], R[1,1], R[1, 2], R[1, 3]
	print R[2,0], R[2,1], R[2, 2], R[2, 3]
	print R[3,0], R[3,1], R[3, 2], R[3, 3]
	return R[i, s + 1], n_panels


def trapezoid(f, a, b, k):
	"""
	This will compute the integral of f(x) from a to b with a recursive
	trapezoidal rule for 2**k panels, using the integral of f(x) from a to b
	computed for 2**(k-1) panels
	"""
	h = (b - a) / k
	x_initial = np.linspace(a, b, k+1)
	f_initial = f(x_initial)
	s = 0.0

	for i in range(1, k):
		s += f_initial[i]
	s = (h / 2) * (f_initial[0] + f_initial[k]) + h*s

	return s;


