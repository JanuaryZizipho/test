from romberg import romberg
import math

def f(x):
	return 2**x

if __name__ == '__main__':
	I, n_panels = romberg(f, 0, 4)
	print I, n_panels
