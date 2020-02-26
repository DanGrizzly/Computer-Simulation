from Polynomials import *

def main():
    polynomialA = Polynomial([2,0,4,-1,6])
    print("Pa(x) is equal to:")
    polynomialA.printPolynomial()

    polynomialB = Polynomial([-1,-3,0,4.5])
    print("Pb(x) is equal to:")
    polynomialB.printPolynomial()

    orderOfPa = polynomialA.orderOf()
    print("Order of Pa(x) is " + str(orderOfPa))

    polynomialA = polynomialA.addPolynomial(polynomialB)
    print("After adding Pb(x) to Pa(x), Pa(x) is equal to:")
    polynomialA.printPolynomial()

    derivativeA = polynomialA.derivate()
    print("The derivative of Pa(x) is equal to:")
    derivativeA.printPolynomial()

    result = derivativeA.antiderivate(2)
    print("The resulting polynomial is:")
    result.printPolynomial()

    polynomialA = Polynomial([5,1,0,2])
    polynomialB = Polynomial([1,0,1,0])
    polynomialA.printPolynomial()
    polynomialB.printPolynomial()
    polynomialA.addPolynomial(polynomialB).printPolynomial()

    
main()

