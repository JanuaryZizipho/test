from scipy.integrate import quad
import trap 
from numpy import inf

def g(t):
	return (-1/ t**2) / (1 + (1/t)**4)

I1 = quad(g, 1, 0)
I2 = trap.trapezoid(g, 1, 0, 0, 5)

if __name__ == '__main__':
	print I1, I2
