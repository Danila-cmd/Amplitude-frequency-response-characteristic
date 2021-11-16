import matplotlib.pyplot as plt
from numpy import *

# 2Pi = 2 * 3,14
DoublePI = float(6.283185306)

# Число отчетов в выбранной трассе
n = 2500

# Временная частота
w = DoublePI/n

# Шаг дискретизации по времени = 0.002
dt = float(2e-3)

# Массивы для значений x и y, для построения графика
data_x = []
data_y = []

# Функция считывания данных и файла формата "515-main.txt"
with open('515-main.txt', 'r') as file:
    # Считывает данные по строчно
    nums = file.readlines()
    nums = [a.rstrip('\n') for a in nums]
for i in range (0, int((n/4)+1), 1):
    a = 0.
    b = 0.
    for j in range(0,n,1):
        # Дискретные коэффициенты Фурье
        a += (2 / n) * float(nums[j]) * cos(w * i * j)
        b += (2 / n) * float(nums[j]) * sin(w * i * j)

    # Амплитудно-частотный спектр
    am = float (a * a + b * b)

    # Частота
    f  = int((i/(n*dt)))

    # Добавляем значения в массивы
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
plt.title("АЧХ")

# Функция построения графика
plt.show()   
