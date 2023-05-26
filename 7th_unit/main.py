# class Cats:
#
#     MAX_AGE = 38
#
#     def __init__(self, name, breed, age):
#         self.name = name
#         self.breed = breed
#         self.age = age
#         self.weight = 0
#         if age > self.MAX_AGE:
#             self.__class__.MAX_AGE = age
#         # Cats.MAX_AGE = age
#
#     def set_weight(self, weight):
#         self.weight = weight
#
#     def print_data(self):
#         print(
#             f'Имя: {self.name}\n'
#             f'Возраст: {self.age}\n'
#             f'Порода: {self.breed}'
#         )
#
#
# murzik = Cats('Мурзик', 'Невская', 3)
# barsik = Cats('Барсик', 'Абиссинская', 1)
#
# murzik.set_weight(10)
# print(murzik.weight)
#
# cat_list = [murzik, barsik]
# for cat in cat_list:
#     cat.print_data()
# import math
#
# x1y1 = (-2, -3)
# x2y2 = (-4, -2)
# length = round(math.sqrt(((x2y2[0] - x1y1[0]) ** 2 + (x2y2[1] - x1y1[1]) ** 2)), 2)
# print(length)
# if x1y1[0] == x2y2[0]:
#     print(False)
# else:
#     print(True)

# name = "Александр Шленский"
# short_name = name.split(" ")[1] + " " + (name.split(" ")[0])[0] + "."
#
# print(short_name)

# tuple1 = ('Разработка', 'УК', 'Автотесты')
#
#
# path_deps = " --> ".join(tuple1)
#
#
# print(path_deps)
