# ������������� �� ������

# �������:
# ���������� ����������� ��������� ��� ������ �� ��������� ���� �����
# ��� ��������� ���������� ������� + ��������� ������

import numpy as np
import matplotlib.pyplot as plt

edge_quality = 6  # ���������� ������ � �������

n = int(input("Coubes quality: "))  # ���������� �������
P_summ = [0] * (n * edge_quality + 1)  # ���������� ��������� ������ �����
max_count_attempts = edge_quality ** n  # ����� ���������� ��������� ������� ������

print("Count_coubes == " + str(n))  # info
print("Count_attempts == " + str(max_count_attempts))
print("Count_possible_value_summ == " + str(len(P_summ)))

for i in range(0, max_count_attempts, 1):
    value = i  # ����� ������
    now_summ = 0  # ����� ��� ������� ������
    while True:
        now_summ += value % edge_quality + 1  # ������� ��� ������� ������
        value = value // edge_quality
        if value == 0:
            break
    P_summ[now_summ] += 1  # �������������� �������� �������� �����

print("Res summ: " + str(P_summ))

  # ���������� � ���������� �������
data_x = []
data_y = []
for i in range(n, len(P_summ), 1):  # ����� �� n �� ����������� (��� ���-�� ����� � ������� ������ 1)
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