from numpy import*
from matplotlib.pyplot import*

n = 50 #number of computations
a = linspace(1,5,n) #array from 1 to 5 with n number of elements
b = linspace(.1,5,n) #the array of i

for i in b: 
    plot(b,a**i-i**a) #operation 
    xlabel('i')
    ylabel('Output (multiple lines for each element in a)')
    title('a^i -i^a for i in 1,2 and a in 1,5')
show()

"""In summary, this takes a list of numbers (a), then does an operation to all of them, 
and plots the output to see how the operation changes the list. Each color on the plot is
the __th entry of each iteration, ie the blue line is all of the first entries"""

#might need to make it s 3D plot, with a,i,output as the 3 axis