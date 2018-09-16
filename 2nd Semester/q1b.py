import newton as new 
import numpy as np
import poly_fit as pf

xdata = np.array([1.8421, 2.4694, 2.4921, 1.9047, 0.8509, -0.4112, -1.5727])
ydata = np.array([0, 0.5, 1, 1.5, 2, 2.5, 3])

m = 3
if __name__ == '__main__':
	p = pf.poly_fit(xdata, ydata, m)

	def f(x):
		return float(p[0] + p[1]*x + p[2]*(x**2) + p[3]*(x**3))
	
	def fprime(x):
		return float(p[1] + 2*p[2]*(x) + 3*p[3]*(x**2))

	r1 = new.newton(f, fprime, 1)
	print(r1)

