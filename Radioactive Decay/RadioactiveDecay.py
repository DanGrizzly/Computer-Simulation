import random

class IodineField:
    
    def __init__(self, λ, n, dt):                               #The initialisation of the field and its values.
        self.λ = λ                                              #Decay constant
        self.n = n                                              #Length of field
        self.dt = dt                                            #Timestep value
        self.p = λ*dt                                           #Probability that an atom will decay.
        self.field = [[1 for i in range(n)] for i in range(n)]  #The field of atoms itself, initialised as all 1s.
        self.halflife = 0                                       #Simulated halflife
        self.decayed = 0                                        #Amount of atoms that have decayed

    def timestep(self):                             
        #Iterate over the field and determine using a random number between 0 and 1 whether the atom will decay
        for y in range(self.n):
            for x in range(self.n):
                if self.field[y][x] == 1:
                    if random.random() < self.p:
                        self.field[y][x] = 0
                        self.decayed += 1
        self.halflife += self.dt     #Add the time passed to the simulated halflife

    def simulate(self):
        #The actual simulation takes place here. We keep going until half the atoms have decayed.
        while self.decayed < ((self.n)**2)/2:
            self.timestep()

        #This is the end of the simulation where we print out the results.
        print()
        self.printfield()
        print()
        print("Initial number of undecayed nuclei:", self.n*self.n)
        print("Final number of undecayed nuclei:  ", self.n*self.n - self.decayed)
        print("Simulated value of the half-life:  ", self.halflife)
        print("Actual value of the half-life:     ", 0.693/self.λ)

    def printfield(self):
        #We simply print the field in terms of 0s and 1s, where 0s are decayed atoms and 1s are undecayed.
        for i in self.field:
            print(''.join(str(j) for j in i)) 


#Prompting the user for input. Should they wish, they can press Enter to use the default values for Iodine-128
try:
    λ = float(input("Please input value for the decay constant λ (or press Enter for default λ = 0.02775): "))
except:
    λ = 0.02775
try:
    n = int(input("Please input value for the length N of the 2D field (or press Enter for default N = 50): "))
except:
    n = 50
try:
    dt = float(input("Please input value for the timestep dt (or press Enter for default dt = 0.01): "))
except:
    dt = 0.01

#Starting the simulation with the given values
IodineField(λ,n,dt).simulate()
