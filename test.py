import numpy as np
from matplotlib.pyplot import*
from matplotlib import cm

def ThreeDee(c,d,e): #this might be a little funky lol, not sure how accurate the average difference part is
    n = 100 #number of computations
    a = np.linspace(0,d,n)
    b = np.linspace(0,e*np.pi,n)[:,np.newaxis]


    fig = figure() 
    ax = fig.add_subplot(projection='3d') # get some 3D axes
    ax.plot_surface(a,b,c,cmap="inferno") # do the surface plot
    ax.set_xlabel('a')
    ax.set_ylabel('b')
    ax.set_zlabel('c')
    show()
    """Given a function (c) of x and y, and the bounds (d,e), this plots the surface of the function"""


from numpy import*
from matplotlib.pyplot import*
from matplotlib import cm

def ThreeDee(c,d,e): #this might be a little funky lol, not sure how accurate the average difference part is
    n = 100 #number of computations
    a = linspace(0,d,n)
    b = linspace(0,e*pi,n)[:,newaxis]


    fig = figure() 
    ax = fig.add_subplot(projection='3d') # get some 3D axes
    ax.plot_surface(a,b,c,cmap="inferno") # do the surface plot
    ax.set_xlabel('a')
    ax.set_ylabel('b')
    ax.set_zlabel('c')
    show()
    """Given a function (c) of x and y, and the bounds (d,e), this plots the surface of the function"""


def PlotList(a_1,a_2,b_1,b_2,n): #lower a bound, upper a bound, lower i bound, upper i bound, number of points
    a = linspace(a_1,a_2,n) #array from a_1 to a_2 with n number of elements
    b = linspace(b_1,b_2,n) #the array of i
    c = []

    for i in b:
        z = a * log(i) #operation
        arr = [i for x in range(len(b))]
        scatter(arr,z) #plotting
        c.append(z) #appending values to a list (for averaging)

    title('Plot of sets under operation')
    xlabel('i')
    ylabel('operation(for every element in a)')
    figure()

    for j in range(n-1): #double for loop since c is list of lists
        tot =[] #list of values (changes for each Liszt in c)
        for k in range(n-1): #find the differences between the elements of c
            d = abs(c[j][k+1]-c[j][k]) #difference
            tot.append(d) 
            avg = sum(tot)/len(tot)


        
        scatter(j,avg)
        
        ylabel('average of differences between elements')
        title('Plot of average of differences between elements of c')
    
    show()
    """Given a list of numbers (a), and a list of operations (b), this plots the output of an operation, 
    to see how an operation changes the spacing in a list, it also plot the average difference between 
    the elements depending on i"""
    #for the given operation, the average of differences is a lil funky...
PlotList(0,2*pi,1,5,100)