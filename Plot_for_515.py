from numpy import *
from matplotlib.pyplot import *

# Массивы для построения графика
data_x = arange(0,5000,2)
data_y = []

# Считываем данные из файла
with open("515-main.txt","r") as file:
    for line in file:
        data_y.append([float(y) for y in line.split()])

# Заносим данные в для пострения графика
plot(data_x, data_y)

# Функция построения графика
show()


