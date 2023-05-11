import math


#Дано 1 число - сторона квадрата.
# Напишите программу, которая рассчитает 3 значения: периметр квадрата, площадь квадрата и диагональ квадрата.
def try_float(value: str) -> float:
    try:
        return float(value)
    except ValueError:
        return None


# Бесконечный цикл
while True:
    side_value = try_float(input("Введите сторону квадрата и нажмите Enter: "))
    if side_value and side_value > 0:
        break


print(f"Периметр квадрата: {4 * side_value}\nПлощадь квадрата: {side_value ** 2}\nДиагональ квадрата: "
      f"{round(side_value * math.sqrt(2), 2)}")

