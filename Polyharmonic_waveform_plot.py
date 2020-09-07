from numpy import *
from matplotlib.pyplot import *

data_x = arange(0,199,2)
data_y = []
with open("ex__104.dat","r") as file:
    for line in file:
        data_y.append([float(y) for y in line.split()])

plot(data_x, data_y)
show()
