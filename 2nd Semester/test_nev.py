from neville import neville

if __name__ == '__main__':
	xdata = [0, 2, 4]
	ydata = [1, 5, 17]

	nev = neville(xdata, ydata, 115) 
	print nev
