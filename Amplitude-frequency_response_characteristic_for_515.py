from math import *
from numpy import *
import matplotlib.pyplot as plt

DoublePI = float(6.283185306)
n = 2500
w = DoublePI/n
dt = float(2e-3)

data_x = []
data_y = []

with open('515-main.txt', 'r') as file:
    nums = file.readlines()
    nums = [a.rstrip('\n') for a in nums]
for i in range (0, int((n/4)+1), 1):
    a = 0.
    b = 0.
    for j in range(0,n,1):
        a += (2 / n) * float(nums[j]) * cos(w * i * j)
        b += (2 / n) * float(nums[j]) * sin(w * i * j)
 
    am = float (a * a + b * b)
    f  = int((i/(n*dt)))
    data_x.append(f)
    data_y.append(am)
 
    print ("w",f,"=","{:6f}".format (am))
    
data_z = [ i * (100/max(data_y)) for i in data_y]

plt.plot(data_x,data_z)
plt.ylabel("Амплитуда")
plt.xlabel("Частота, Гц")

plt.grid(True, linewidth=1,linestyle = '-.')

plt.title("АЧХ")
plt.show()   
