def trapezoid(f, a, b, Iold, k):
	"""This will compute the integral of f(x) from a to b with a recursive
	trapezoidal rule for 2**k panels, using the integral of f(x) from a to b
	computed for 2**(k-1) panels

	Arguments:
	f -- the integrand
	a -- the lowr limit
	b -- the upper limit

	"""

	if k == 1:
		Inew = (f(a) + f(b)) * (b - a) / 2.0
	else:
		n = 2 ** (k - 2)
		h = (b - a) / n
		x = a + h / 2.0
		s = 0.0
		for i in range(n):
			s += f(x)
			x += h
		Inew = (Iold + h *s) / 2.0

	return Inew

