import matplotlib.pyplot as plt
import numpy as np

# Считывание данных

file_in = open("line.txt", 'r')

data_x = []
data_y = []
for line in file_in:
    data_x.append(float(line.split(" ")[0]))
    data_y.append(float(line.split(" ")[1]))

file_in.close()

# Вычисления

A = np.array([[0, 0], [0, 0]], 'f')
B = np.array([[0], [0]], 'f')

for i in range(0, len(data_x), 1):
    A[0][0] += (data_x[i] * data_x[i])
    A[0][1] += data_x[i]
    A[1][0] += data_x[i]
    B[0][0] += data_x[i] * data_y[i]
    B[1][0] += data_y[i]

A[1][1] = len(data_x)

inv_A = np.linalg.inv(A)    # Обратная матрица

X = inv_A.dot(B)    # Перемножение матриц

print(X)

# Расчет точек для прямой

line_x = []
line_y = []

line_x.append(data_x[0])
line_y.append(X[0][0] * line_x[0] + X[1][0])

line_x.append(data_x[len(data_x) - 1])
line_y.append(X[0][0] * line_x[1] + X[1][0])

# Построение графика

plt.figure()

plt.subplot(1, 1, 1)
plt.title("Line")
plt.plot(data_x, data_y, label="Line", marker='*')
plt.plot(line_x, line_y, label="Line", marker='^')

plt.legend()
plt.show()