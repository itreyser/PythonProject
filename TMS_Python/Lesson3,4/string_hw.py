# Работа со строками
# 1
var_str = "Hello world Slava"
print(var_str[0])
print(var_str[-1])
print(var_str[2])
print(var_str[-3])
print(len(var_str))
# 2
song_var = "If you play, you play for keeps."
print(song_var[0:8])
print(song_var[13:17])
print("символы с индексами кратными трем:", song_var[0::3])
print("Перевернутая строка: ", song_var[::-1])
# 3
var_str = "my name is name"
new_var = var_str.split(" ")
new_var[3] = "Slava"
var_str = " ".join(new_var)
print(var_str)
# 4
test_string = "Hello world!"
print(test_string.find("w"))
print(len(test_string))
print(test_string.startswith("Hello"))
print(test_string.endswith("qwe"))

