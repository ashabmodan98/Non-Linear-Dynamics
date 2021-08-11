import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

f = lambda x,y,z:sigma*(y-x)
g = lambda x,y,z:r*x-y-x*z
j = lambda x,y,z:x*y-b*z

r,sigma,b=28,10,8/3 #beyond the Hopf bifurcation

h=0.01
t=np.arange(0,100,h)
n=10000

x1 = np.ones(n)
y1 = np.ones(n)
z1 = np.ones(n)
z1plusones = []
x2 = np.ones(n)
y2 = np.ones(n)
z2 = 1.00001*np.ones(n)


#x1[0]=float(input('Enter the x value of the 1st initial condition: ' ))
#y1[0]=float(input('Enter the y value of the 1st initial condition: ' ))
#z1[0]=float(input('Enter the z value of the 1st initial condition: ' ))

for i in range (0,n-1):
	k11 = h * f(x1[i],y1[i],z1[i])
	k21 = h * g(x1[i],y1[i],z1[i])
	k31 = h * j(x1[i],y1[i],z1[i])

	k12 = h* f(x1[i] + 0.5*k11,y1[i] + 0.5*k21, z1[i] + 0.5*k31)
	k22 = h* g(x1[i] + 0.5*k11,y1[i] + 0.5*k21, z1[i] + 0.5*k31)
	k32 = h* j(x1[i] + 0.5*k11,y1[i] + 0.5*k21, z1[i] + 0.5*k31)

	k13 = h* f(x1[i] + 0.5*k12,y1[i] + 0.5*k22, z1[i] + 0.5*k32)
	k23 = h* g(x1[i] + 0.5*k12,y1[i] + 0.5*k22, z1[i] + 0.5*k32)
	k33 = h* j(x1[i] + 0.5*k12,y1[i] + 0.5*k22, z1[i] + 0.5*k32)

	k14 = h * f(x1[i] + k13, y1[i] + k23, z1[i] + k33)
	k24 = h * g(x1[i] + k13, y1[i] + k23, z1[i] + k33)
	k34 = h * j(x1[i] + k13, y1[i] + k23, z1[i] + k33)
    
	x1[i+1] = x1[i] + (k11 + 2*k12 + 2*k13 + k14)/6
	y1[i+1] = y1[i] + (k21 + 2*k22 + 2*k23 + k24)/6
	z1[i+1] = z1[i] + (k31 + 2*k32 + 2*k33 + k34)/6
	z1plusones.append(z1[i+1])
	

#x2[0]=float(input('Enter x of 2nd initial condition: ' ))
#y2[0]=float(input('Enter y of 2nd initial condition: ' ))
#z2[0]=float(input('Enter z of 2nd initial condition: ' ))

for i in range (0,n-1):
	k11 = h * f(x2[i],y2[i],z2[i])
	k21 = h * g(x2[i],y2[i],z2[i])
	k31 = h * j(x2[i],y2[i],z2[i])

	k12 = h* f(x2[i] + 0.5*k11,y2[i] + 0.5*k21, z2[i] + 0.5*k31)
	k22 = h* g(x2[i] + 0.5*k11,y2[i] + 0.5*k21, z2[i] + 0.5*k31)
	k32 = h* j(x2[i] + 0.5*k11,y2[i] + 0.5*k21, z2[i] + 0.5*k31)

	k13 = h* f(x2[i] + 0.5*k12,y2[i] + 0.5*k22, z2[i] + 0.5*k32)
	k23 = h* g(x2[i] + 0.5*k12,y2[i] + 0.5*k22, z2[i] + 0.5*k32)
	k33 = h* j(x2[i] + 0.5*k12,y2[i] + 0.5*k22, z2[i] + 0.5*k32)

	k14 = h * f(x2[i] + k13, y2[i] + k23, z2[i] + k33)
	k24 = h * g(x2[i] + k13, y2[i] + k23, z2[i] + k33)
	k34 = h * j(x2[i] + k13, y2[i] + k23, z2[i] + k33)
    
	x2[i+1] = x2[i] + (k11 + 2*k12 + 2*k13 + k14)/6
	y2[i+1] = y2[i] + (k21 + 2*k22 + 2*k23 + k24)/6
	z2[i+1] = z2[i] + (k31 + 2*k32 + 2*k33 + k34)/6

X = np.zeros(n)
X1 = np.empty(2500) #to store the first values for linear fit
t1 = np.empty(2500)
for j in range(0,n):
	X[j] = np.log(math.sqrt((x2[j]-x1[j])**2 + (y2[j]-y1[j])**2 + (z2[j]-z1[j])**2))

X1 = X[:2500] #slicing to obtain the first 25 values to fit them
t1 = t[:2500] #to make the dimensions same;and the values until 25 is the linear part

z = np.polyfit(t1, X1, 1) #now z is the function which is assigned the fitted values
m = np.polyfit(t1, X1, 1) #degree of fitting set to 1
p = np.poly1d(z)
print("slope: ",m)

#3d figures plot
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot3D(x1, y1, z1, 'b')
ax.set_title("First Initial Cond")
#plt.show()
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot3D(x2, y2, z2, 'g')
ax.set_title("Second Initial Cond")
plt.show()

plt.plot(t,z1)
plt.xlim(10,25)
plt.show()

#lyapnov exponent plot
fig,(ax1,ax2) = plt.subplots(2,1, figsize=(7,20))
ax1.plot(t,X)
ax1.set_xlim([0,50])
ax1.set_title("Lyapnov Exponent")

ax2.plot(t,X,'r',t1,p(t1),'b')
ax2.set_xlim([0,25])
ax2.set_ylim([-13,4])
ax2.set_title("Fitted Lyapnov exponent")
plt.show()

