import numpy as np
import matplotlib.pyplot as plt
import random
from mpl_toolkits import mplot3d

def f(x,y,a,b):
    return -x+a*y+x**2*y
def g(x,y,a,b):
    return b-a*y-x**2*y

a,b=0.08,0.6

h=0.01
t=np.arange(0,100,h)
n=10000

x=np.empty(n)
y=np.empty(n)

#fig = plt.figure() #for the 3D plot
#ax = plt.axes(projection='3d')

#inputing the parameters
#a=float(input('Enter the value for parameter a: '))
#b=float(input('Enter the value for parameter b: '))	

"""
input the initial condition
x[0]=float(input('Enter the x value of the initial condition: '))
y[0]=float(input('Enter the y value of the initial condition: '))	
"""

for j in range(100):
    initial_x=random.uniform(0, 4)
    initial_y=random.uniform(0, 4)
    x[0]=initial_x
    y[0]=initial_y
	
    for i in range (0,n-1):
        k11 = h * f(x[i],y[i],a,b)
        k21 = h * g(x[i],y[i],a,b)
    
        k12 = h * f(x[i] + 0.5*k11,y[i] + 0.5*k21,a,b)
        k22 = h * g(x[i] + 0.5*k11,y[i] + 0.5*k21,a,b)

        k13 = h * f(x[i] + 0.5*k12,y[i] + 0.5*k22,a,b)
        k23 = h * g(x[i] + 0.5*k12,y[i] + 0.5*k22,a,b)

        k14 = h * f(x[i] + k13,y[i] + k23,a,b)
        k24 = h * g(x[i] + k13,y[i] + k23,a,b)
     
        x[i+1] = x[i] + (k11 + 2*k12 + 2*k13 + k14)/6
        y[i+1] = y[i] + (k21 + 2*k22 + 2*k23 + k24)/6    
        
    #ax.plot3D(x,y,t)
    plt.plot(x,y,'b')
#plt.xlim(0,4)
#plt.ylim(0,4)
plt.show()

