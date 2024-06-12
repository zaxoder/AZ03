
# 2. Построй диаграмму рассеяния для двух наборов случайных данных, сгенерированных с помощью
# функции `numpy.random.rand`.
# import numpy as np
# random_array = np.random.rand(5)  # массив из 5 случайных чисел
# print(random_array)
# 3. Необходимо спарсить цены на диваны с сайта divan.ru в csv файл,
# обработать данные, найти среднюю цену и вывести ее, а также сделать
# гистограмму цен на диваны

import matplotlib.pyplot as plt
import numpy as np

mean = 0
std_dev = 1
num_samples = 1000

data = np.random.normal(mean, std_dev, num_samples)

plt.hist(data, bins=30, edgecolor='black')

plt.title('Гистограмма нормального распределения случайных данных')
plt.xlabel('Значение')
plt.ylabel('Частота')

plt.show()
