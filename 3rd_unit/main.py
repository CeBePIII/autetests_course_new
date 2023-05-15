import math
# num = '1234'
# mid_number = list(map(int, num))
# print(mid_number)
# prod = math.prod(list(map(int, num)))
# print(prod, type(prod))


num = 4
count_multy = 0
lenth_flag = len(str(num))
if lenth_flag == 0:
    count_multy = 0
else:
    while lenth_flag > 1:
        multiplayed = 1
        for index in str(num):
            multiplayed *= int(index)
        num = multiplayed
        print(num)
        count_multy += 1
        print(count_multy)
        lenth_flag = len(str(num))

