
import numpy as np
import matplotlib.pyplot as plt


def f(x,r):
    return r*x*(1-x)

r1=float(input('Enter the value of r:' ))

n=10000
r = np.linspace(2.9,4,n)  #for plotting the graph for x vs r initializing the values of r
iterations=1000 
first=100 #assuming that the system approaches the stable after the first
#100 iterations were period doubling starts for 2 cycle
x=1e-5*np.ones(n)   
lamda=np.empty(n)

#to plot the x vs n diagram for a particular r
n1=100
x1=np.empty(n1)
k=0.1
t=np.arange(0,10,k)
x1[0]=0.01
for i in range(n1-1): #for finding the xns
	x1[i+1] = f(x1[i],r1)
plt.plot(t,x1)
plt.xlim(0,8)
plt.ylim(0,1.1)
plt.title("Logistic Map")
plt.show()

fig,(ax1,ax2) = plt.subplots(2,1, figsize=(7,20)) #the number of subplots grids we set in the figure =2*1

for i in range(iterations-1): #for finding the xns
    x = f(x,r)
                                                                                
    if i >= (iterations - first): #plotting only for the iterations after it has stabilised
        ax1.plot(r, x, ',k', alpha=.25) #orbit diagram
    #Lyapunov Exponent
    lamda = lamda + np.log(abs(r-2*r*x))
    ax2.plot(r,lamda,color='green')
   
ax1.set_title("Bifurcation Diagram")
ax1.set_xlim([2.9,4])
ax2.set_title("Lyapnov Exponent")
ax2.set_xlim([2.9,4])
plt.show()


