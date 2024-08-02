import scipy.integrate as integrate

def adaptive_integration(func, a, b, tol=1e-5):
    result, _ = integrate.quad(func, a, b, epsabs=tol)
    return result

def main():
    func = lambda x: x**2
    print("Integral of x^2 from 0 to 1:", adaptive_integration(func, 0, 1))

main()
