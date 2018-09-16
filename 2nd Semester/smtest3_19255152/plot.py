import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy import stats

def plot():
	xdata = np.array([0.50, 1.00, 1.50, 2.00, 2.50])
	ydata = np.array([0.49, 1.55, 3.26, 6.74, 10.16])

	f1 = interp1d(xdata, ydata)
	f2 = interp1d(xdata, ydata, kind="cubic")
#	slope, intercept, r_value, p_value, std_err = stats.linregress(xdata, ydata)

	xplot = np.linspace(0.0, 3.0, 40)

	fig, ax = plt.subplots()
	ax.plot(xdata, ydata, "ro")
 
	plt.show()

if __name__ == '__main__':
    plot()
