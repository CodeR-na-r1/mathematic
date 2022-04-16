#   Студенты борются за автомат

import numpy as np

total_attempts = 4500   # Количество запусков программы (кол-во иммитаций игры)
quantity = 100   # Количество студентов и коробок для них

total_wins = 0   # Счетчик побед студентов

now_attempt = 0   # Счетчик текущей игры (попытки) студентов
print("Calc ...", end='')
while now_attempt < total_attempts:   # Имитируем заданное количество попыток

    num_students = np.arange(quantity)   # Номера студентов
    boxes = np.random.permutation(quantity)   # Коробки со случайными номерами

    flag_win = True   # Флаг, отвечающий за уловие победы

    i = 0   # Счетчик текущего студента

    while (i < quantity):
        index = i   # Счетчик номера студента, который он вытаскивает (для вложенного цикла)
        counter = 0   # Счетчик попыток студента
    
        while (num_students[i] != boxes[index]):   # Пока студент не вытащил свой номер из коробки
            index = boxes[index]   # Студент достает свой номер из коробки
            counter += 1   # Инкремент счетчика попыток студента
            if (counter >= 50):   # Если попытки кончились, то поражение
                flag_win = False
                break

        if (flag_win == False):   # Выход из цикла перебора попыток студента к циклу перебора студентов
            break
   
        i += 1   # Инкремент счетчика текущего студента

    if (flag_win):   # Инкремент счетчика побед студентов
        total_wins += 1

    now_attempt += 1   # Инкремент счетчика текущей иммитации игры

print("\rThe probability of students winning: " + str((total_wins - 0) * (100 - 0) / (total_attempts - 0) + 0) + "%\n")   # Выввод получившиеся вероятности (со встроенной формулой функции map ддя преобразования в проценты)