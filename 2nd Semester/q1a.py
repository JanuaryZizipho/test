import cspline as c
import numpy as np 

x = 1.5
xdata = np.array([1, 2, 3, 4, 5])
ydata = np.array([0, 1, 0, 1, 0])

if __name__ == '__main__':
	k = c.curvatures(xdata, ydata)
	val = c.eval_spline(xdata, ydata, k, x)
	print val
