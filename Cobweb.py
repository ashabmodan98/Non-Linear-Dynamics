import matplotlib.pyplot as plt
import numpy as np
from math import sin
from math import pi

def f(r,x):
	return r*x*(1-x)
#f2 = np.vectorize(f)

n=100
r=float(input('r: '))

x=np.linspace(0,1)
t=np.linspace(0,1)
x=0.11 

fig, ax =plt.subplots(1,1)
ax.plot(t, f(r,t),'k') #plots the inverted parabola
ax.plot([0,1],[0,1],'k') #plotting the straight line

for j in range(n):
        y=f(r,x)
        ax.plot([x,x],[x,y],'r',lw=1)
        ax.plot([x,y],[y,y],'r',lw=1)
        x=y
        
plt.show()
