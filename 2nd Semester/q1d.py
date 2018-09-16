import cspline as c
import numpy as np
import math

xdata = np.array([0, 0.5, 1, 1.5, 2])
ydata = np.array([-0.7854, 0.6529, 1.7390, 2.2071, 1.9425])
x1 = math.pi / 4.0
x2 = math.pi / 2.0

if __name__ == '__main__':
	k = c.curvatures(xdata, ydata)
	y1 = c.eval_spline(xdata, ydata, k, x1)
	y2 = c.eval_spline(xdata, ydata, k, x2)
	print y1,  y2
