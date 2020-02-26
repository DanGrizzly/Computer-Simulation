"""
This file contains the mandelbrot class which is capable of rendering a plot of a mandelbrot set given the resolution and iteration limit.
After the class definition we just create a Mandelbrot object and plot it.
Uses matplotlib and numpy additional python libraries.
Also contains the Julia class for plotting the Julia set.
"""

import numpy as np
import matplotlib.pyplot as plt

class Mandelbrot:

    def __init__(self, resolution, iterations):
        self.resolution = resolution                            #Amount of points that will be calculated on x and y axis. Points calculated = resolution^2
        self.iterations = iterations                            #Upper iteration limit

    #Function to determine whether a point {x,y} belongs to mandelbrot set
    def mandelbrot(self, x, y):
        n = 0
        c = x + 1j*y                                            #Point represented as a complex number C
        z = c
        for i in range(self.iterations):
            n = i
            z = z**2 + c
            if abs(z) > 2:
                break
        return n                                                #Return amount of iterations it took for point to to "diverge"

    def plotMandelbrot(self):
        vectorizedMandelbrot = np.vectorize(self.mandelbrot)    #Vectorize the mandelbrot function
        X = np.linspace(-2.025, 0.6, self.resolution)           #Spread points over the x axis
        Y = np.linspace(-1.125, 1.125, self.resolution)         #Spread points over the y axis

        #Create a plane/grid from x and y axes.
        XX, YY = np.meshgrid(X,Y)

        #Calculate N values using vectorized function
        N = vectorizedMandelbrot(XX, YY)

        #Create the plot over the extent of points calculated
        plt.imshow(N, extent = (X.min(), X.max(), Y.min(), Y.max()))
        plt.xlabel('r')                                         #Real number line on the x axis
        plt.ylabel('i')                                         #Imaginary number line on the y axis
        plt.show()                                              #Render plot


class Julia:
    def __init__(self, resolution, iterations, shape):
        self.resolution = resolution                            #Amount of points that will be calculated on x and y axis. Points calculated = resolution^2
        self.iterations = iterations                            #Upper iteration limit
        self.shape      = shape                                 #Tuple represting a complex number, shape is the value of C which will determine the shape of the Julia set
                                                                #Some famous Julia values: (-1,0), (0.5,0), (0,-1), (0.36,0.1), (-0.1,0.8)

    #Function to determine whether a point {x,y} belongs to mandelbrot set
    def julia(self, x, y):
        n = 0
        c = self.shape[0] + 1j*(self.shape[1])
        z = x + 1j*y
        for i in range(self.iterations):
            n = i
            z = z**2 + c
            if abs(z) > 2:
                break
        return n                                                #Return amount of iterations it took for point to to "diverge"

    def plotJulia(self):
        vectorizedJulia = np.vectorize(self.julia)              #Vectorize the julia function
        X = np.linspace(-2, 2, self.resolution)                 #Spread points over the x axis
        Y = np.linspace(-1.5, 1.5, self.resolution)             #Spread points over the y axis

        #Create a plane/grid from x and y axes.
        XX, YY = np.meshgrid(X,Y)

        #Calculate N values using vectorized function
        N = vectorizedJulia(XX, YY)

        #Create the plot over the extent of points calculated
        plt.imshow(N, extent = (X.min(), X.max(), Y.min(), Y.max()))
        plt.xlabel('r')                                         #Real number line on the x axis
        plt.ylabel('i')                                         #Imaginary number line on the y axis
        plt.show()                               

#Render the Mandelbrot plot with resolution 500 and iteration bound 255.
Mandelbrot(500,55).plotMandelbrot()
#Julia(500,255,(0.5,0)).plotJulia()
