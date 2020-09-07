from math import *
import matplotlib.pyplot as plt

with open('100.txt', 'r') as file:
    nums = file.readlines()
    nums = [a.rstrip('\n') for a in nums]

jl=[]
js=[]

n = 50

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
  jl.append(j)
  js.append(s)
  print (j, s, sep = "\t")

plt.plot(jl, js)
plt.show()
