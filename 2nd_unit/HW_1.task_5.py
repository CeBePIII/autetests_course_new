#Дано 2 числа a и b. Используя форматирование строк, выведите на экран их сумму и
# произведение в форматах ’a + b = c’ и ’a*b = c’.

a_number = int(input("Введите число a: "))
b_number = int(input("Введите число b: "))

sum_result = a_number + b_number
mult_result = a_number * b_number
print(f"{a_number} + {b_number} = {sum_result}\n{a_number} * {b_number} = {mult_result}")
