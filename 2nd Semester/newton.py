def newton(f,fprime,p,tol=1e-15,n=100):
    i = 1
    while abs(0 - f(p)) > tol and i <= n:
			p = p - 1.0*f(p)/fprime(p)
			i += 1
    return p

def f(x):
    return x**3 + 4*x**2 - 10

def fprime(x):
    return 3*x**2 + 8*x

#if __name__ == '__main__':
 #   r1 = newton(f, fprime,1)
 #   print (r1)
