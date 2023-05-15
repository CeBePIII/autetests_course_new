# Задача Иосифа Флавия
# https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B4%D0%B0%D1%87%D0%B0_%D0%98%D0%BE%D1%81%D0%B8%D1%84%D0%B0_%D0%A4%D0%BB%D0%B0%D0%B2%D0%B8%D1%8F
# Задача заключается в следующем: по кругу стоит num_people воинов,
# начиная с первого воина они выводят из круга каждого kill_num по счёту.
# Вы должны правильно указать, кто является «выжившим», то есть: последний элемент списка.
#
# num_people=7, kill_num=3 => Значит 7 человек в кругу и каждый третий из него выходит
# [1,2,3,4,5,6,7] - начальный круг
# [1,2,4,5,7] => 3 и 6 вышел
# [1,4,5] => 2 и 7 вышел
# [1,4] => 5 вышел
# [4] => 1 вышел, 4 остался последним т.е. выжившим - это наш ответ survivor.

def josephus_task(num_people, kill_num):
    step_index = 0
    peoples = [i for i in range(1, num_people + 1)]
    while len(peoples) > 1:
        loosers = []
        passed = 0
        if len(peoples) + step_index < kill_num:
            step_index += len(peoples)
        for index, value in enumerate(peoples, 1 + step_index):
            passed += 1
            if index % kill_num == 0:
                loosers.append(value)
                step_index = len(peoples) - passed
        for looser in loosers:
            if len(peoples) > 1:
                peoples.remove(looser)
    return peoples[0]

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [
    (7, 3), (11, 19), (1, 300), (14, 2), (100, 1), (1234, 56), (987, 11)
]

test_data = [
    4, 10, 1, 13, 100, 1130, 379
]


for i, d in enumerate(data):
    assert josephus_task(*d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')