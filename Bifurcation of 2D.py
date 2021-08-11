import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


def f(x,y,a):
    return y + 1 -a*x*x
def g(x,y,b):
    return b*x

n=10000
a = np.linspace(0.5,1.5,n)
b = 0.3 
iterations=1000 
first=200
x = 1e-5*np.ones(n)
y = 1e-5*np.ones(n)

fig = plt.figure()
ax = plt.axes(projection='3d')

for i in range(iterations-1): #for finding the xns
    x = f(x,y,a)
    y = g(x,y,b)
    
    if i >= (iterations - first): #plotting only for the iterations after it has stabilised
        ax.plot3D(a, x, y,  ',k', alpha=.25) #orbit diagram

ax.set_xlabel('a axis')
plt.show()




