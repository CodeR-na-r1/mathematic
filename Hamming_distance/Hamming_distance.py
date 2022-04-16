# Расстояние Хэминга
# Считать с файла, проаналазировать и вывести наиболее устойчивый к ошибкам код Хэмминга.

    # Функция для подсчёта расстояния хэминга в между двумя щифрами
def calc_distance_code(first_code, second_code):
    res = 0
    for i in range(0, len(first_code), 1):
        if first_code[i] != second_code[i]:
            res += 1
    return res

# ------------- Блок считывания с файла -------------

data_file = open('Control/input3.dat', 'r')

count_codes = len(data_file.readline().split(' ')) - 1    # Количество шифров, учавствующих в сравнении

arr_codes = []
for i in range(0, count_codes, 1):
    arr_codes.append([])

data_file.seek(0)

for line in data_file:    # Считывание шифров
    part_row = line.split(' ')

    for i in range(0, count_codes, 1):
        arr_codes[i].append(part_row[i + 1].split('\n')[0])

data_file.close()

print(arr_codes)

distance_codes = [0] * count_codes    # Общее расстояние хэмминга шифра
min_distance_codes = [99999] * count_codes    # Минимальное расстояние Хэмминга в шифре
avg_distance_codes = [0] * count_codes    # Среднее значение расстоний Хэммтнга в шифе

for i in range(0, count_codes, 1):    # Перебор наборов кодов
    for j in range(0, len(arr_codes[i]) - 1, 1):    # Перебор кодов внутри шифра
        for z in range(j + 1, len(arr_codes[i]), 1):    # Перебор кодов внутри шифра
            value = calc_distance_code(arr_codes[i][j], arr_codes[i][z])    # Вычисление расстояния между кодами внутри шифра и подсчет параметров
            distance_codes[i] += value
            if value < min_distance_codes[i]:
                min_distance_codes[i] = value
            avg_distance_codes[i] += value
    avg_distance_codes[i] /= len(arr_codes[i])

print("\nValues of distance:\t\t\t" + str(distance_codes))
print("Min values inside a code:\t\t" + str(min_distance_codes))
print("Average values inside a distance:\t" + str(avg_distance_codes))

# ------------- Блок анализа результатов -------------

best_values = [0] * count_codes
for i in range(0, count_codes, 1):    # Запоминаем лучшие результаты
    if (distance_codes[i] > best_values[0]):
        best_values[0] = distance_codes[i]

    if (min_distance_codes[i] > best_values[1]):
        best_values[1] = min_distance_codes[i]

    if (avg_distance_codes[i] > best_values[2]):
        best_values[2] = avg_distance_codes[i]

        
score_codes = [0] * count_codes
for i in range(0, count_codes, 1):    # Подсчет рейтинга между кодами
    if (distance_codes[i] == best_values[0]):
        score_codes[i] += 1
        
    if (min_distance_codes[i] == best_values[1]):
        score_codes[i] += 2

    if (avg_distance_codes[i] == best_values[2]):
        score_codes[i] += 1

best = 0
best_codes = []
for i in range(0, count_codes, 1):    # Ищем лучшие коды
    if (score_codes[i] == best):
        best_codes.append(i + 1)

    if (score_codes[i] > best):
        best = score_codes[i]
        best_codes = [i + 1]

print("Bests number of codes === " + str(best_codes))    # Вывводим лучшие коды