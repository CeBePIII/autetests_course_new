#Дана строка. Напишите программу удаления символов, которые имеют нечетные значения индекса заданной строки.
#
# while True:
#     string = input("Введите строку: ")
#     if len(string) > 0:
#         break
#
# print(string[::2])

#другой способ
string = input("Введите строку: ")
list2display = []
for index, value in enumerate(string):
    if index % 2:
        list2display.append(value)
string2display = "".join(list2display)
print(string2display)
