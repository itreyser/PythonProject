# Работа с циклами

# 1
a = int(input("Введите число А "))
b = int(input("Введите число Б "))
counter = 0
for i in range(a, b + 1):
    counter += i
print(counter)

# 2
a = int(input("Введите число А "))
b = int(input("Введите число Б "))
counter2 = 0
for i in range(a, b + 1):
    if i > 0:
        counter2 += i
print(counter2)

# 3
multiplication_counter = 1
sum_counter = 0
negative_numbers = 0
for i in range(10):
    num = int(input())
    if num > 0:
        multiplication_counter *= num
        sum_counter += num
    else:
        negative_numbers += 1
print("Сумма положительных чисел: ", sum_counter)
print("Умножение положительных чисел: ", multiplication_counter)
print("Количество отрицательных чисел: ", negative_numbers)

# 4
result_max = 0
results_dict = {
    "Бекиш Александр": 21.07,
    "Будник Алексей": 20.34,
    "Гребень Анастасия": 22.12,
    "Давидович Татьяна": 30.00,
    "Дешук Дмитрий": 24.01,
    "Казак Анна": 28.17
}
for i in results_dict:
    if result_max < results_dict[i]:
        result_max = results_dict[i]
print(result_max)

# 5
list_uniq = [1, 5, 2, 9, 2, 9, 1]
counter = 0
for i in list_uniq:
    if i == list_uniq[-1]:
        for j in range(0, len(list_uniq)):
            if i == j:
                counter += 1
    else:
        for j in range(i + 1, len(list_uniq)):
            if i == j:
                counter += 1
    if counter > 1:
        print("Уникальное число -", list_uniq[i])
