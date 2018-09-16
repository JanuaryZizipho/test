from scipy.integrate import quad
import numpy as np
import math

def g(x):
	return x**(-1/4) * math.sin(x)

I1 = quad(g, 0, 1)
#I2 = trap.trapezoid(g, 0, 1, 0, 5)

if __name__ == '__main__':
	print I1
