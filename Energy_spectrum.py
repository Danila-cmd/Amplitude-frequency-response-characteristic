import matplotlib.pyplot as plt
from numpy import *

# 2Pi = 2 * 3,14
DoublePI = float(6.283185306)

# Число отчетов в выбранной трассе
n = 99 #Put number of traces

# Временная частота
w = DoublePI/n

# Шаг дискретизации по времени = 0.002
dt = float(2e-3)

# Массивы для значений x и y, для построения графика
data_x = []
data_y = []

# Функция считывания данных и файла формата "1.txt"
with open('1.txt', 'r') as file: #Put name of file consist of traces 
    nums = file.readlines()
    nums = [a.rstrip('\n') for a in nums]
for i in range (0, int((n/4)+1), 1):
    a = 0.
    b = 0.
    for j in range(0,n,1):

        # Фурье-коэффициент
        a += (2 / n) * float(nums[j]) * cos(w * i * j)

    # Энергетический спектр
    am = float ((a * a))   
    f  = int((i/(n*dt)))
    data_x.append(f)
    data_y.append(am)

    # Выводим значения в консоль
    print ("w",f,"=","{:6f}".format (am))

# Отображение в процентах
data_z = [ i * (100/max(data_y)) for i in data_y]

# Задаем параметры для графика
plt.plot(data_x,data_z)
plt.ylabel("Амплитуда")
plt.xlabel("Частота, Гц")

# Задаем параметры сетки на графике
plt.grid(True, linewidth=1,linestyle = '-.')

# Заголовок графика
plt.title("Энергетический спектр")

# Функция построения графика
plt.show() 
