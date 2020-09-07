from math import *
from numpy import *
import matplotlib.pyplot as plt

DPI = float(6.283185306)
n = 100
w = DPI/n
dt = float(2e-3)

data_x = []
data_y = []

with open('ex__104.dat', 'r') as file:
    nums = file.readlines()
    nums = [a.rstrip('\n') for a in nums]
for i in range (0, int((n/4)+1), 1):
    a = 0.
    b = 0.
    for j in range(0,n,1):
        a += (2 / n) * float(nums[j]) * cos(w * i * j)
        b += (2 / n) * float(nums[j]) * sin(w * i * j)
 
    am = float (sqrt(a * a + b * b))
    f  = int((i/(n*dt)))
    
    data_x.append(f)
    data_y.append(am)
    print ("w",f,"=","{:6f}".format (am))

plt.bar(data_x,data_y,width=5)
plt.ylabel("Амплитуда")
plt.xlabel("Частота, Гц")

plt.grid(True, linewidth=1,linestyle = '-.')

plt.title("АЧХ")
plt.show()   
