# Работа со списками

# 1
list1 = [1, 2, 3, 4, 5]
list2 = [345, 56756, 87978, 345345]
# 2
print(list1[2])
# 3
list2[-1] = 666
print(*list2)
# 4
list3 = list1 + list2
print(list3)
# 5
list4 = list3[3:]
print(list4)
# 6
list4.append(88)
list4.append(7777)
print(list4)
# 7
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
common_elements = list(set(a) & set(b))

print(common_elements)
# 8
list5 = [1, 2, 3, 4, 3, 2, 5, 1, 4, 6, 7, 1, 8, 2, 3]
set1 = set(list5)
list5 = list(set1)
print(list5)
