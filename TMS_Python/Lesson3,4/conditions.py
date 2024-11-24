# Работа с условиями
from itertools import count

# 1
num = 5
if num >= 0:
    num += 1
print(num)

# 2
num_1 = 3
num_2 = -2
num_3 = 5
count = 0
if num_1 > 0:
    count += num_1
if num_2 > 0:
    count += num_2
if num_3 > 0:
    count += num_3
print(count)

# 3
year = int(input("Введите год: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("366 дней")
        else:
            print("365 дней")
    else:
        print("365 дней")
else:
    print("365 дней")

# 4
num_5 = int(input("Введите число от 1 до 7: "))
if num_5 == 1:
    print("Понедельник")
elif num_5 == 2:
    print("Вторник")
elif num_5 == 3:
    print("Среда")
elif num_5 == 4:
    print("Четверг")
elif num_5 == 5:
    print("Пятница")
elif num_5 == 6:
    print("Суббота")
else:
    print("Воскресенье")
# 5
unit_number = int(input("Введите номер единицы массы (1-5): "))
mass = float(input("Введите массу тела в этих единицах: "))
if unit_number == 1:
    # Килограммы
    print(mass)
elif unit_number == 2:
    # Миллиграммы
    print(mass * 0.000001)
elif unit_number == 3:
    # Граммы
    print(mass * 0.001)
elif unit_number == 4:
    # Тонны
    print(mass * 1000)
elif unit_number == 5:
    # Центнеры
    print(mass * 100)
else:
    raise ValueError("Неверный номер единицы измерения. Должно быть от 1 до 5.")
