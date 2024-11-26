# Преобразование типов

# 1
var_str = "Robin Singh"
var_str2 = "I love arrays they are my favorite"
print(var_str.split(" "))
print(var_str2.split(" "))
# 2

list1 = ['Ivan', 'Ivanou']
str1 = "Minsk"
str2 = "Belarus"
greeting = f"Привет, {list1[0]} {list1[1]}! Добро пожаловать в {str1} {str2}"
print(greeting)
# 3
list2 = ["I", "love", "arrays", "they", "are", "my", "favorite"]
list_to_str = " ".join(list2)
print(list_to_str)
# 4
list_for_hw = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_for_hw[2] = 66
list_for_hw.pop(5)
print(list_for_hw)
# 5
a = {'a': 1, 'b': 2, 'c': 3}
b = {'c': 3, 'd': 4, 'e': 5}
ab = {}
all_keys = set(a.keys()).union(set(b.keys()))

for key in all_keys:
    value_a = a.get(key, None)
    value_b = b.get(key, None)

    ab[key] = [value_a, value_b]

print(ab)