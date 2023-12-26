"""
Created on Tue Dec  7 17:35:01 2021
In this program we are using Monte Carlo program to estimate the value of Pi.

Theory: Area of Square(As)=a^2
        Area of the circle(Ac)=pi*r^2=pi(a/2)^2 as r=a/2
        (Ac/As)=(no of points inside the circle)/total no of points
        Finally pi= 4*(no of points inside the circle)/total no of points
        *Increasing the number of points increases the accuracy of the 
        approximation.

Das_Proj.py
@author: abinashdas
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig=plt.figure(figsize=(10,10))

N=200000 # Total number of random points that will be generated.

N_circle=0  # This is a counter to count the number of points inside the circular region

"""
In the following code segment we generate random values for x and y coordinates
and then we store these values in two arrays
"""
x=np.random.uniform(size=N) # x-coordinate array
y=np.random.uniform(size=N) # y-coordinates array
    
"""
In the next segment of the code we plot a rectangle as well the inscribed 
circle. The square that we choose here is of unit length starting with it 
below left corner from (0,0). 
We again choose the circle of radius 0.5 cm, centred at (0.5,0.5)
"""
draw=fig.add_subplot()
# Drawing the rectangle
rect = patches.Rectangle((0, 0), 1, 1, linewidth=3, edgecolor='r', facecolor='none')
draw.add_patch(rect)

# Drawing the Circle
circle= patches.Circle((0.5, 0.5), 0.5, linewidth=2, edgecolor='y', facecolor='none')
draw.add_patch(circle)


"""
In the next segment we use the generated x and y values, and segregate them 
into four arrays a set of two for the points inside the circle and the others 
for points outside. Here we extracts the point using masking. In the last part 
the function we plot the inside and the outside points.

"""
# The x and y coordinate array for the points inside the circle
# By using masking we change the values in array
# And we use the formula (x-c1)^2+(x-c2)^2 where (c1,c2) are the centr of the 
# circle.
insidex=x[((x-0.5)**2+(y-0.5)**2)<0.5**2] 
insidey=y[((x-0.5)**2+(y-0.5)**2)<0.5**2]
    
# The x and y coordinate for the points outside the circle
outsidex=x[((x-0.5)**2+(y-0.5)**2)>=0.5**2]
outsidey=y[((x-0.5)**2+(y-0.5)**2)>=0.5**2]

# Plotting the points.
draw.plot(insidex,insidey,'go') #plotting the inside points in green
draw.plot(outsidex,outsidey,'ro') # plotting the outside points in red

"""
Here we calculate the total number of points inside the circle by using the 
len function for any of the array for inside coordinates of points. In this case we use the 
x-coordinate array for the inside coordinates. Then finally we find the value of pi.
"""    
N_circle=N_circle+len(insidex) # Total number of points inside circle.

pi=4*N_circle/N # Calculating the approximate value of pi.

print(f"The approximate value of pi is {pi}")
