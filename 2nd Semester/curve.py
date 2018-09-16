import cubic_spline as cs
import matplotlib.pyplot as plt
import neton_poly as npoly
import numpy as np

def draw():
	xdata = np.array([])
	ydata = np.array([])

	#cubic spline
	k = cs.curvatures(xdata, ydata)
	xs = np.linearspace(0.9, 13.3, 1000)
	yc = np.array([cs.eval_spline(xdata, ydat, k, x) for x in xs])

	#Newton's polynomial
	a = npoly.coefficients(xdata, ydata)
	yp = np.array([npoly.eval_poly(a, xdata, a) for x in xs])

	

