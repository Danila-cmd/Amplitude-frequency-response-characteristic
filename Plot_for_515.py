from numpy import *
from matplotlib.pyplot import *

data_x = arange(0,5000,2)
data_y = []
with open("515-main.txt","r") as file:
    for line in file:
        data_y.append([float(y) for y in line.split()])

plot(data_x, data_y)
show()


