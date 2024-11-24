# работа с while циклами
from itertools import count

#1
N = int(input("Введите число N: "))
product = 1
i = 1
while i <= N:
    product *= i
    i += 1
print(product)

#2
S1 = float(input("Введите начальную площадь первого сорта (S1): "))
S2 = float(input("Введите начальную площадь второго сорта (S2): "))
years = 0

while S1 >= 0.1 * S2:
    S1 *= 2
    S2 *= 3
    years += 1


print("Через", years, "лет площадь первого сорта будет составлять меньше 10% от площади второго сорта.")

#3
num = int(input("Введите число: "))
count = 0
sum_digit = 0
while num > 0:
    count += 1
    sum_digit += num % 10
    num //= 10

print("Количество цифр:", count)
print("Сумма цифр:", sum_digit)
