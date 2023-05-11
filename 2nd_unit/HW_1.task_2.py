#Дано квадратное уравнение x^2+bx+c=0.
#Дискриминант уравнения должен быть больше 0.
#Напишите программу, которая найдет корни квадратного уравнения и округлит их до 2 знаков после запятой.

print("Квадратное уравнение ax\u00B2 + bx + c")
a = float(input("Введите a: "))
b = float(input("Введите b: "))
c = float(input("Введите c: "))

# Вычисляем дискриминант
D = b ** 2 - 4 * a * c
# Вычисляем корни, если они есть
if D <= 0:
    print("Не удалось высчитать корни")
else:
    result1 = (-b + D ** (1 / 2))/2 * a
    result2 = (-b - D ** (1 / 2))/2 * a
    print(f"Корни уравнения:\n {result1}\n{result2}")



