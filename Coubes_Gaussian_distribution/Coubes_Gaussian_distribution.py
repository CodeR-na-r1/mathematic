# Распределение по Гауссу

# Задание:
# Подсчитать вероятность вхождений для каждой из возможных сумм очков
# для заданного количества кубиков + построить график

import numpy as np
import matplotlib.pyplot as plt

edge_quality = 6  # Количество граней у кубиков

n = int(input("Coubes quality: "))  # Количество кубиков
P_summ = [0] * (n * edge_quality + 1)  # Колиечство выпаданий каждой суммы
max_count_attempts = edge_quality ** n  # Общее колиечство возможных исходов броска

print("Count_coubes == " + str(n))  # info
print("Count_attempts == " + str(max_count_attempts))
print("Count_possible_value_summ == " + str(len(P_summ)))

for i in range(0, max_count_attempts, 1):
    value = i  # Номер броска
    now_summ = 0  # Сумма при текущем броске
    while True:
        now_summ += value % edge_quality + 1  # Подсчет для каждого кубика
        value = value // edge_quality
        if value == 0:
            break
    P_summ[now_summ] += 1  # Инкрементируем значение выпавшей суммы

print("Res summ: " + str(P_summ))

  # Подготовка к построению графика
data_x = []
data_y = []
for i in range(n, len(P_summ), 1):  # Сумма до n не заполняется (мин кол-во очков с каждого кубика 1)
    data_x += [i + 1]
    data_y += [P_summ[i] / max_count_attempts]

print("Probability summ: " + str(data_y))

plt.figure()

plt.subplot(1, 1, 1)
plt.title("Dependence of Summ value to Probability")
plt.xlabel('Summ value')
plt.ylabel('Probability')
plt.plot(data_x, data_y, label="Coubes", marker='^')

plt.legend()
plt.show()