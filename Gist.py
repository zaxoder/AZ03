import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(5)
y = np.random.rand(5)

plt.scatter(x, y)

plt.title("Диаграмма рассеяния случайных данных")
plt.xlabel("Значения X")
plt.ylabel("Значения Y")

plt.show()
