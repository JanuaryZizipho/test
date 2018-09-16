import newton
import numpy as np

def root(a, k):
	
	def f(x):
		return x**k - a

	def fprime(x):
		return k*x**(k-1)

	r1 = newton.newton(f, fprime, 1)
	print r1

#if __name__ == '__main__':
#	root(100,5)
