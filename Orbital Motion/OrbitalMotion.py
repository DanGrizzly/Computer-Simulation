"""
This code contains two classes and one main function.
It contains an Object class to represent a Planet/Asteroid in the Simulation,
and a Simulation class that runs the simulation itself and draws it on a plot.
The main function reads simulation parameters from OrbitalMotionParameters.txt,
initiates a Simulation object and then runs the code.

It can also save an animation, given that a certain line is uncommented.
(Commented by default)

The parameters for additional objects of mass Mi and distance from Mars Ri
MUST be put in this format (Use only whole numbers or the exponential form):
Mi = _number here_
Ri = _number here_
"""

import matplotlib.pyplot as plt
import math
import numpy as np
import matplotlib.animation as animation
import ast
import ffmpeg


class Simulation:                                   #Class for the Physical Simulation

    def __init__(self,dt=1,G=6.67*10**-11,r=3e7):   #Initialises the simulation given parameters, if unspecified, default ones will be used.
        self.dt = dt                                #The timestep between each frame
        self.G = G                                  #The Gravitational constant, if the user wishes to experiment with it.
        self.r = r                                  #The radius up to which the simulation can be seen. set to 3e7 by default.
        self.objects = []                           #Objects inside the simulation
        self.patches = []                           #Objects to be drawn and animated on the plot.

    def addObject(self, obj):                       #Function to add an object to the simulation
        self.objects.append(obj)

    def timestep(self,frames):                      #Function that is called every frame.
        global phobosperiods
        global phobosperiod
        periodbool = False

        #Adjust the velocities of all objects inside the simulation based on other objects in the system
        for i in range(len(self.objects)):
            for j in range(len(self.objects)):
                if i == j:
                    continue
                else:
                    self.objects[i].v += self.acceleration(self.objects[i],self.objects[j])*self.dt

        #This part is used to help calculate the period of Phobos manually. We will need another part after the position of Phobos is updated
        if len(self.objects) > 1:
            if self.objects[1].p[1] < 0:        #Calculate Phobos' period by finding in what time it passes through the x axis from negative y to positive y.
                periodbool = True

        #Adjusting positions of all objects and updating them.
        for i in range(len(self.objects)):
            self.objects[i].p += self.objects[i].v*self.dt
            self.patches[i].center = tuple(self.objects[i].p)

        #This part is used to help calculate the period of Phobos manually. Prints out the period in hours.
        if len(self.objects) > 1:
            if periodbool and (self.objects[1].p[1] >= 0):
                print("Simulated phobos period =",((frames*self.dt-phobosperiod)/60)/60,"hours")
                phobosperiod = frames*self.dt

        #Prints out the Kinetic energy of the system every 1000 frames.
        if(frames%1000==0):
            print("Kinetic energy =",self.kineticEnergy(),"Joules")

        #Returns the 'patches' (objects to draw) to draw on the plot each frame.
        return self.patches

    #Function that computes the acceleration that a given object receives from another due to gravity.
    def acceleration(self,obj1,obj2):
        return ((self.G*(obj2.m))/(Object.distance(obj1,obj2)))*((obj2.p-obj1.p)/math.sqrt(Object.distance(obj1,obj2)))

    #Function called at start of animation. Merely returns the patches to draw at the start.
    def initAnimation(self):
        return self.patches

    #Function that calculates the Kinetic energy of the System. It should fluctuate since orbits aren't perfect circles and because we aren't taking Potential energy into account.
    def kineticEnergy(self):
        K = 0
        for obj in self.objects:
            K += (1/2)*(obj.m)*(sum(obj.v**2))
        return K

    #Function that initiates the plot and starts the simulation
    def simulate(self):
        global phobosperiod
        phobosperiod = 0

        #Functions to customise the plot.
        plt.style.use('dark_background')
        fig = plt.figure()
        ax = plt.axes()
        ax.axis('scaled')
        ax.set_xlim(-self.r,self.r)
        plt.xlabel('meters')
        ax.set_ylim(-self.r,self.r)
        plt.ylabel('meters')

        #Add all objects to patches to be drawn as circles.
        for obj in self.objects:
            self.patches.append(plt.Circle(obj.p,obj.size,color = obj.color, animated = True))
        for i in self.patches:
            ax.add_patch(i)

        #Starts the animation with initAnimation and keeps it going every frame by calling the timestep function.
        #blit = True speeds up the simulation by only redrawing parts that are changed. Recommended to keep True.
        anim = animation.FuncAnimation(fig,self.timestep,init_func=self.initAnimation,frames=10**6,repeat=True,interval = 1, blit = True)
        #anim.save("aaa.mp4")   #Saves the animation. If uncommented, please set repeat = False on the line above.

        #Show the plot in a new window.
        plt.show()


class Object:
    
    def __init__(self,m,p,v,size, color):       #Initialises an Object object given parameters for
        self.m = m                              #Mass of object
        self.p = np.array(p,dtype=float)        #Position of object, given as an array or tuple of length 2.
        self.v = np.array(v,dtype=float)        #Velocity of object, given as an array or tuple of length 2.
        self.size = size                        #Size of the object. Relevant only for drawing purposes.
        self.color = color                      #Color of the object. Relevant only for drawing purposes.

    @staticmethod                               #Function to calculate distance between two objects. Static method because it makes sense for it to be here.
    def distance(obj1,obj2):
        return sum((obj1.p-obj2.p)**2)


#Function to read parameters and initialise Simulation object.
def main():
    #Read parameters and store them into contents.
    contents = open("OrbitalMotionParameters.txt","r").read().splitlines()
    G  = ast.literal_eval(contents[0][5:])
    dt = ast.literal_eval(contents[1][5:])
    m1 = ast.literal_eval(contents[2][5:])

    #Initialise Simulation given the parameters
    MarsSim = Simulation(dt,G)
    MarsSim.addObject(Object(m1,(0,0),(0,0),3000000, 'orangered'))

    #Read remaining and optional objects from contents
    for i in range((len(contents)-4)//2):
        m = ast.literal_eval(contents[4+2*i][5:])
        r = ast.literal_eval(contents[5+2*i][5:])
        if r == 0:
            pass
        else:
            #For the additional objects, they are given a starting velocity in the positive y direction, calculated based on orbital velocity sqrt(G*m/r)
            obj = Object(m,(r,0),(0,math.sqrt((G*m1)/r)),2*10**5, 'white')
            MarsSim.addObject(obj)

    #Start the simulation
    MarsSim.simulate()

main()
