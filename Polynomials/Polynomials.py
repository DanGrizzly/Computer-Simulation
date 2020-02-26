class Polynomial:

    def __init__(self, values):
        #Initialises the polynomial and ensures that there are no trailing zeros.
        #If there were trailing zeros, the order function would be wrong.
        zeros = 0                           #Variable used locally purely to determine amount of trailing zeros in the input
        while values[-zeros-1] == 0:
            zeros += 1
        if zeros > 0:
            self.coeffs = values[:-zeros]   #coeffs is a list used to represent the coefficients of the polynomial.
        else:                               
            self.coeffs = values            

    def orderOf(self):
        #Returns the order of the polynomial based on its length 
        return len(self.coeffs) - 1

    def addPolynomial(self, q):
        #Adds a polynomial to itself and returns a new polynomial.
        values = []
        #The addition is done by summing the lists of the coefficients of the two polynomials. We need to know which polynomial is smaller so we don't run out of range in the loop.
        if len(self.coeffs) < len(q.coeffs):
            for i in range(len(self.coeffs)):
                values.append(self.coeffs[i] + q.coeffs[i])
            for i in q.coeffs[(len(self.coeffs)):]:
                values.append(i)
        else:
            for i in range(len(q.coeffs)):
                values.append(self.coeffs[i] + q.coeffs[i])
            for i in self.coeffs[(len(q.coeffs)):]:
                values.append(i)
        return Polynomial(values)   #Because __init__ is called here, we don't have to worry about creating a polynomial with trailing zeros.
        
    def derivate(self):
        #Function to calculate the derivative form, simply by multiplying each entry by its order and shortening the list by 1.
        values = []
        for i in range(1, len(self.coeffs)):
            values.append(i*self.coeffs[i])
        return Polynomial(values)

    def antiderivate(self, c):
        #Function to calculate the antiderivative form, by dividing each entry by its order and adding the value of c to the beggining of the list
        values = []
        for i in range(len(self.coeffs)):
            values.append(self.coeffs[i]/(i+1))
        values.insert(0,c)
        return Polynomial(values)

    def printPolynomial(self):
        #Function to print the polynomial
        strings = []
        for i in range(len(self.coeffs)):
            if i == 0:
                strings.append(str(self.coeffs[0]))
            elif i == 1:
                strings.append(str(self.coeffs[1])+"x")
            else:
                strings.append(str(self.coeffs[i])+"x^"+str(i))
        strings = filter(lambda x: x[0] != '0', strings)
        print(" + ".join(strings))
