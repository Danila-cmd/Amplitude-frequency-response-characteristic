from math import *
from numpy import *
import matplotlib.pyplot as plt

n = 50

with open('100.txt', 'r') as file:
  nums = file.readlines()
  nums = [a.rstrip('\n') for a in nums]
  
js=[]

for k in range(0, 2* n - 1, 1):
  j= k-n+1
  s=0
  for i in range(0, n, 1):
    l=i+j
    if ((l < 0) or (l > n - 1)):
      ft = 0
    else:
      ft =float(nums[l])
      s +=(float(nums[i]) * ft)
        
  js.append(s)

DoublePI = float(6.283185306)
n= 99
w = DoublePI/n
dt = float(2e-3)

data_x = []
data_y = []


for i in range (0, int((n/4)+1), 1):
  a = 0.
  for j in range(0,n,1):
    
    a += (2 / n) * float(js[j]) * cos(w * i * j)
    
  P = float((a * a))    
  f  = int((i/(n*dt)))
  data_x.append(f)
  data_y.append(P)

  print ("w",f,"=","{:6f}".format (P))

data_z = [ i * (100/max(data_y)) for i in data_y]

plt.plot(data_x,data_z)
plt.ylabel("Амплитуда")
plt.xlabel("Частота, Гц")

plt.grid(True, linewidth=1,linestyle = '-.')

plt.title("Энергетический спектр")
plt.show()
